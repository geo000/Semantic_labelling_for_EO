import numpy as np

class S2SpectralIndex:
    def __init__(self,
                 band1, band2, band3, band4, band5,
                 band6, band7, band8, band9, band10,
                 band11, band12, band13):

        # Copernicus Sentinel 2
        self.ultra_blue = band1
        self.blue = band2
        self.green = band3
        self.re1 = band4
        self.re2 = band5
        self.re3 = band6
        self.NIR = band7
        self.NIRn = band8
        self.Water_vapor = band9
        self.SWIR_cirrus = band10
        self.SWIR1 = band11
        self.SWIR2 = band12
        self.band12 = band13

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




