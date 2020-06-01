# EO toolkit for Semantic Data Labelling 

## Spectral Indicies

Class containing indicies for sentinel 2 data. 
This will be updated every now and then.

## Requesting data from Sentinel Hub API

All the code required to obtain sentinel 2 data is [here](https://github.com/ThomasJames/Spectral_Indices/blob/master/data_request.py)
The ```SentinelRequest``` class contains methods to obtain a single image of all bands, or a large batch of images of a specified band. 

## Prerequisite

This program is works with numpy arrays:

```
pip install numpy
pip install sentinelhub
pip install matplotlib
pip install rifffile
pip install scikit-image
pip install pillow
pip install opencv-python
```
### Error handling

- Program checks that input is numpy array.

- Program checks that image dimensions are consistent.


## Inputs

Copernicus Sentinel 2 bands.
Inputs must be numpy arrays. 

Specific information about sentinel 1A and sentinel 2A/B can be found [here](https://earth.esa.int/web/sentinel/technical-guides/sentinel-2-msi/msi-instrument)

<img src="https://github.com/ThomasJames/Spectral_Indices/blob/master/S2_bands.png" width="500">
(ESA)

Futher information about sentinel 2 is [here](https://sentinel.esa.int/documents/247904/685211/Sentinel-2+Products+Specification+Document+%28PSD%29/0f7bedeb-9fbb-4b60-91aa-809162de456c)

## Normalised Difference Water Index (NDWI) - Example:
<img src="https://github.com/ThomasJames/Spectral_Indices/blob/master/Normalised%20Difference%20Water%20Index.png" width="500">

## Indices

Normalised Build up Difference Index (Zha et al., 2007)

Modified Normalised Difference Water Index (Xu, 2006)

Normalised Difference Water Index (McFeeters, 1996)

Normalized Difference Fraction (Boschetti et al., 2014)

Water Ratio Index (Shen and Li, 2010)

## SAR-MSI Index fusion algorithm

Used for semantic labelling for CNN training

```
Water index label:
WI = ((i * ((SWIR2 - NIR) / (SWIR2 + NIR))) +
      (j*((green - SWIR2) / (green + SWIR2))) +
      (k * ((green - NIR) / (green + NIR)))) + (l * SAR)
      
Built up index label
NDBI = (SWIR2 - NIR) / (SWIR2 + NIR)
```
<img src="https://github.com/ThomasJames/Spectral_Indices/blob/master/Combined.png" width="500">

## Training tile extraction

For this project I wanted to extract 244x244 mask, ans 244x244x3 (true color) tiles for the VGG-16 network so I built this function. 
It can be scaled to any tile size. 

```
def split_image(dim_pix, im, location, dtype, filename):
    # Find the number of sub-images that fit in rows
    rows = []
    for i in range((math.floor(im.shape[0] / dim_pix))):
        rows.append(i)
    # Find the number of sub-images that fit in rows
    columns = []
    for i in range((math.floor(im.shape[1] / dim_pix))):
        columns.append(i)

    # Numerically identify the sub-image
    a = 0
    for i in rows:
        for j in columns:

            # Check for 244 x 244 (Mask) or 244 x 244 x 3 (TC image)
            if im[0 + (dim_pix * j): dim_pix + (dim_pix * j),
                  0 + dim_pix * i: dim_pix + (dim_pix * i)].shape == \
                    (dim_pix, dim_pix) or (dim_pix, dim_pix, 3):

                # Save the 244 x 244 as an tiff file.
                imsave(f"{filename}/{location}_{region}_{a}_{dtype}.tiff",
                        im[0 + (dim_pix * j): dim_pix + (dim_pix * j),
                        0 + dim_pix * i: dim_pix + (dim_pix * i)])
                a += 1
            else:
                print("no data")
```




