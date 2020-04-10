

class SpectralIndex:
    def __init__(self,
                 s2band1, s2band2, s2band3, s2band4, s2band5,
                 s2band6, s2band7, s2band8, s2band9, s2band10,
                 s2band11, s2band12, s2band13, c1, c2, D1, D2, L):

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

        self.c1 = c1
        self.c2 = c2
        self.D1 = D1
        self.D2 = D2
        self.L = L

    """  
    Enhanced Vegetation Index
    (Liu & Huete, 1995; Xue et al., 2017)
    """
    def EVI(self):
        return 2.5 * ((self.NIR -self.red) /
                      (self.NIR + self.c1 * self.red - self.c2 * self.blue + self.L))

    """  
    Automated Water Extraction Index
    Feyisa et al., 2014
    """

    def AWEI(self):
        return self.C1 * (self.green - self.SWIR1) - \
               (self.c2 * self.NIR * self.SWIR2)

    """        
    Automated Water Extraction Index - Removal of shadow pixels
    Feyisa et al., 2014
    """

    def AWEIsh(self):
        return self.blue + self.D1 * self.green - \
               self.D2 * (self.NIR + self.SWIR1) - self.D3 * self.SWIR2

    """
    Modified Normalised Difference Water Index
    Xu, 2006
    """

    def MNDWI(self):
        return (self.green - self.SWIR1) / (self.green + self.SWIR1)

    """
    Normalised Difference Water Index
    McFeeters, 1996
    """

    def NDWI(self):
        return (self.green - self.NIR) / (self.green / self.NIR)

    """
    USE: Flooding
    Boschetti et al., 2014
    """

    def NDFI(self):
        return (self.green - self.SWIR2) / (self.green / self.SWIR2)

    """"
    Soil Adjusted Vegetation Index
    Heute, 1988
    """

    def SAVI(self):
        return (1 + self.L) * (self.NIR + self.red + self.L)

    """"
    Soil Adjusted total Vegetation Index
    Heute, 1988
    """

    def SAVI(self):
        return (1 + self.L) * (self.NIR + self.red + self.L)

    """  
    Water Ratio Index
    Shen and Li, 2010
    """

    def WRI(self):
        return (self.green + self.red) / (self.NIR + self.SWIR1)

    """  
    Soil - Adjusted Vegetation Index optimized
    for Agricultural Monitoring
    """

    def OSAVI(self):

    def FCD(self):

    def BI(self):

    def SI(self):

    def TI(self):


