import numpy as np
import matplotlib.pyplot as plt

# Extract True Color image
TC = np.load("TC-Region2.npy")
TC = TC[-1]

# Extract SAR IW
SAR = np.load("SAR-Region2.npy")
SAR = SAR[-1][:, :, 1]

bs = 0.006
SAR[SAR > bs] = 1
SAR[SAR < bs] = 0


# Extract MSI bands
MSI = np.load("MSI-Region2.npy")
blue = MSI[-1][:, :, 1]
green = MSI[-1][:, :, 2]
red = MSI[-1][:, :, 3]
NIR = MSI[-1][:, :, 7]
SWIR1 = MSI[-1][:, :, 10]
SWIR2 = MSI[-1][:, :, 11]


# Water Index
i = 1
j = 1.0
k = 1.0
l = 0.3

WI = ((i * ((SWIR2 - NIR) / (SWIR2 + NIR))) +
      (j*((green - SWIR2) / (green + SWIR2))) +
      (k * ((green - NIR) / (green + NIR)))) + (l * SAR)
WI[WI > 0] = 1
WI[WI < 0] = 0

# Built up index
NDBI = (SWIR2 - NIR) / (SWIR2 + NIR)
NDBI[NDBI > 0] = 2
NDBI[NDBI < 0] = 0

COM = NDBI + WI
COM[COM == 3] = 0

'''
0 = No label
1 = Water
2 = Buildings
'''

plt.imsave("WI.png", WI, cmap="Blues")
plt.imsave("NDBI.png", NDBI, cmap="Reds")
plt.imsave("Combined.png", COM, cmap="Pastel2")
plt.imsave("SAR.png", SAR, cmap="Blues")
plt.imsave("TC.png", TC)






















