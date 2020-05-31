import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt
from skimage.transform import rescale
import skimage.color as color

"""
dim_pix - Dimensions of the target image (Model input)
im - 2D numpy array to be split
Location - A string to save the location of the image
dytpe - String to describe (Label or input)
"""


def split_image(dim_pix, im, location, dtype, filename):
    rows = []
    for i in range((math.floor(im.shape[0] / dim_pix))):
        rows.append(i)
    columns = []
    for i in range((math.floor(im.shape[1] / dim_pix))):
        columns.append(i)
    a = 0
    for i in rows:
        for j in columns:
            plt.imsave(f"{filename}/{a}{dtype}{location}.png",
                       im[0 + (dim_pix * j): dim_pix + (dim_pix * j),
                       0 + dim_pix * i: dim_pix + (dim_pix * i)],
                       cmap="Blues")
            a += 1


"""
Proposed Water index (WI)
i - NBDI (Zha et al., 2007)
j - PI (Jain et al., 2020)
k - PI (Jain et al., 2020)
l - SAR Scalar 
"""
def WI(SWIR2, NIR, green, SAR, i, j, k, l):
    WI = ((i * ((SWIR2 - NIR) / (SWIR2 + NIR))) +
          (j * ((green - SWIR2) / (green + SWIR2))) +
          (k * ((green - NIR) / (green + NIR)))) + (l * SAR)
    WI[WI > 0] = 1
    WI[WI < 0] = 0
    return WI

# i - NBDI (Zha et al., 2007)
def NDBI(SWIR2, NIR):
    NDBI = (SWIR2 - NIR) / (SWIR2 + NIR)
    NDBI[NDBI > 0] = 1
    NDBI[NDBI < 0] = 0
    return NDBI

if __name__ == "__main__":

    region = "3"

    # Extract True Color image
    TC = np.load(f"TC-Region{region}.npy")
    TC = TC[-1]

    # Extract SAR IW
    SAR = np.load(f"SAR-Region{region}.npy")
    SAR = SAR[-1][:, :, 1]

    bs = 0.006
    SAR[SAR > bs] = 1
    SAR[SAR < bs] = 0

    # Extract MSI bands
    MSI = np.load(f"MSI-Region{region}.npy")
    blue = MSI[-1][:, :, 1]
    green = MSI[-1][:, :, 2]
    red = MSI[-1][:, :, 3]
    NIR = MSI[-1][:, :, 7]
    SWIR1 = MSI[-1][:, :, 10]
    SWIR2 = MSI[-1][:, :, 11]

    # Water Index
    i = 0.0
    j = 1.0
    k = 1.0
    l = 0.0

    WI = ((i * ((SWIR2 - NIR) / (SWIR2 + NIR))) +
          (j * ((green - SWIR2) / (green + SWIR2))) +
          (k * ((green - NIR) / (green + NIR)))) + (l * SAR)
    WI[WI > 0] = 1
    WI[WI < 0] = 0

    # Save the images
    plt.imsave("WI.png", WI, cmap="Blues")
    plt.imsave("SAR.png", SAR, cmap="Blues")
    plt.imsave("TC.png", TC)

    # Split and export the training images and labels
    split_image(dim_pix=244, im=WI, location="Shanghai", dtype="Mask", filename=f"Region_{region}")
    split_image(dim_pix=244, im=TC, location="Shanghai", dtype="TC", filename=f"Region_{region}")


