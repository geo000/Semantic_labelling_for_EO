import numpy as np

class SpectralIndex:
    def __init__(self,
                 s2band1, s2band2, s2band3, s2band4, s2band5,
                 s2band6, s2band7, s2band8, s2band9, s2band10,
                 s2band11, s2band12, s2band13):

        # Copernicus Sentinel 2
        self.ultra_blue = s2band1
        self.blue = s2band2
        self.green = s2band3
        self.re1 = s2band4
        self.re2 = s2band5
        self.re3 = s2band6
        self.NIR = s2band7
        self.NIRn = s2band8
        self.Water_vapor = s2band9
        self.SWIR_cirrus = s2band10
        self.SWIR1 = s2band11
        self.SWIR2 = s2band12
        self.band12 = s2band13

    """
    normalized difference built-up index 
    Zha et al., 2007
    """
    def NBDI(self):
        top = np.subtract(self.SWIR1, self.NIRn)
        bottom = np.add(self.SWIR1, self.NIRn)
        return np.divide(top, bottom)

    """
    Modified Normalised Difference Water Index
    Xu, 2006
    """
    def MNDWI(self):
        top = np.subtract(self.green, self.SWIR1)
        bottom = np.add(self.green, self.SWIR1)
        return np.divide(top, bottom)

    """
    Normalised Difference Water Index
    McFeeters, 1996
    """

    def NDWI(self):
        top = np.subtract(self.green, self.NIR)
        bottom = np.add(self.green, self.NIR)
        return np.divide(top, bottom)

    """
    Normalized Difference Fraction
    USE: Flooding
    Boschetti et al., 2014
    """
    def NDFI(self):
        top = np.subtract(self.green, self.SWIR2)
        bottom = np.add(self.green, self.SWIR2)
        return np.divide(top, bottom)

    """  
    Water Ratio Index
    Shen and Li, 2010
    """
    def WRI(self):
        top = np.add(self.green, self.red)
        bottom = np.add(self.NIR, self.SWIR1)
        return np.divide(top, bottom)




