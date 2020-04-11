import numpy as np

class S2SpectralIndex:
    def __init__(self,
                 B01, B02, B03, B04, B05,
                 B06, B07, B08, B09, B10,
                 B11, B12):

        # Copernicus Sentinel 2
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
        return np.divide(np.subtract(self.SWIR1, self.NIRn), (np.add(self.SWIR1, self.NIRn)))
        
    """
    Modified Normalised Difference Water Index
    Xu, 2006
    """
    def MNDWI(self):
        return np.divide(np.subtract(self.green, self.SWIR1)), (np.add(self.green, self.SWIR1))

    """
    Normalised Difference Water Index
    McFeeters, 1996
    """

    def NDWI(self):
        return np.divide(np.subtract(self.green, self.NIR), (np.add(self.green, self.NIR)))

    """
    Normalized Difference Fraction
    USE: Flooding
    Boschetti et al., 2014
    """
    def NDFI(self):
        return np.divide(np.subtract(self.green, self.SWIR2), np.add(self.green, self.SWIR2))

    """  
    Water Ratio Index
    Shen and Li, 2010
    """
    def WRI(self):
        return np.divide((np.add(self.green, self.red)), (np.add(self.NIR, self.SWIR1)))


    """
    Soil Adjusted Vegetation Index
    """
    def SAVI(self):
        L = 0.428
        return (np.subtract(self.NIRn, self.re1)), (np.add(self.NIRn, self.re1)) * (1.0 + L)

    """ 
    SIPI (Structure Insensitive Pigment Index)
    """

