import numpy as np


class S2SpectralIndex:
    def __init__(self,
                 B01=None, B02=None, B03=None, B04=None, B05=None,
                 B06=None, B07=None, B08=None, B09=None, B10=None,
                 B11=None, B12=None):

        # Check the arguments are numpy arrays.
        arg = np.array([B01, B02, B03, B04, B05, B06, B07, B08, B09, B10, B11, B12])
        for i in range(len(arg)):
            if arg[i] is None:
                continue
            elif type(arg[i]).__module__ != np.__name__:
                print("Input of band ", str(i + 1), "must be a numpy array")

        # Check for consistency in dimensions.
        dim = []
        for i in range(len(arg)):
            if arg[i] is not None:
                dim.append(arg[i].shape)
        if len(set(dim)) > 1:
            print("Check dimensions")

        self.ultra_blue = B01
        self.blue = B02
        self.green = B03
        self.re1 = B04
        self.re2 = B05
        self.re3 = B06
        self.NIR = B07
        self.NIRn = B08
        self.Water_vapor = B09
        self.SWIR_cirrus = B10
        self.SWIR1 = B11
        self.SWIR2 = B12

    """
    normalized difference built-up index 
    Zha et al., 2007
    """

    def NBDI(self):
        try:
            return np.divide(np.subtract(self.SWIR1, self.NIRn), (np.add(self.SWIR1, self.NIRn)))
        except IOError:
            print("Check you have loaded in the right bands")

    """
    Modified Normalised Difference Water Index
    Xu, 2006
    """

    def MNDWI(self):
        try:
            return np.divide(np.subtract(self.green, self.SWIR1)), (np.add(self.green, self.SWIR1))
        except IOError:
            print("Check you have loaded in the right bands")

    """
    Normalised Difference Water Index
    McFeeters, 1996
    """

    def NDWI(self):
        try:
            return np.divide(np.subtract(self.green, self.NIR), (np.add(self.green, self.NIR)))
        except IOError:
            print("Check you have loaded in the right bands")

    """
    Normalized Difference Fraction
    USE: Flooding
    Boschetti et al., 2014
    """

    def NDFI(self):
        try:
            return np.divide(np.subtract(self.green, self.SWIR2), np.add(self.green, self.SWIR2))
        except IOError:
            print("ERROR: Image dimensions are not consistent")

    """  
    Water Ratio Index
    Shen and Li, 2010
    """

    def WRI(self):
        try:
            return np.divide((np.add(self.green, self.red)), (np.add(self.NIR, self.SWIR1)))
        except IOError:
            print("Check you have loaded in the right bands")

    """
    Soil Adjusted Vegetation Index
    HUETE, 1988
    """

    def SAVI(self):
        L = 0.428
        try:
            return np.divide((np.subtract(self.NIRn, self.re1), (np.add(self.NIRn, self.re1)) * (1.0 + L)
        except IOError:
            print("Check you have loaded in the right bands")

if __name__ == "__main__":
    """
    Simple example - Two numpy 3 x 3 arrays representing images with consistent pixel dimensions.
    In this case a = band 11 (short wave infrared 1), b = band 8 (Near Infrared)
    The test case is the normalized difference built-up index.
    """
    a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    b = np.array([[1, 2, 4], [3, 2, 2], [6, 3, 3]])

    z = S2SpectralIndex(B11=a, B08=b)
    z_NBDI = z.NBDI()
    print(z_NBDI)
