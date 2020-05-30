# Spectral Indicies

Class containing indicies for sentinel 2 data. 
This will be updated every now and then.

# Requesting data from Sentinel Hub API

All the code required to obtain sentinel 2 data is [here](https://github.com/ThomasJames/Spectral_Indices/blob/master/data_request.py)
The ```SentinelRequest``` class contains methods to obtain a single image of all bands, or a large batch of images of a specified band. 

## Prerequisite

This program is works with numpy arrays:

```
pip install numpy
pip install sentinelhub
pip install matplotlib
```
### Error handling

- Program checks that input is numpy array.

- Program checks that image dimensions are consistent.


## Inputs

Copernicus Sentinel 2 bands.
Inputs must be numpy arrays. 

Specific information about sentinel 1A and sentinel 2A/B can be found [here](https://earth.esa.int/web/sentinel/technical-guides/sentinel-2-msi/msi-instrument)

![](https://github.com/ThomasJames/Spectral_Indices/blob/master/S2_bands.png)
(ESA)

Futher information about sentinel 2 is [here](https://sentinel.esa.int/documents/247904/685211/Sentinel-2+Products+Specification+Document+%28PSD%29/0f7bedeb-9fbb-4b60-91aa-809162de456c)

## Normalised Difference Water Index (NDWI) - Example:

![](https://github.com/ThomasJames/Spectral_Indices/blob/master/Normalised%20Difference%20Water%20Index.png)


## Indices

Normalised Build up Difference Index (Zha et al., 2007)

Modified Normalised Difference Water Index (Xu, 2006)

Normalised Difference Water Index (McFeeters, 1996)

Normalized Difference Fraction (Boschetti et al., 2014)

Water Ratio Index (Shen and Li, 2010)

# SAR-MSI Index fusion algorithm

Used for semantic labelling for CNN training

```
Water index label:
WI = ((i * ((SWIR2 - NIR) / (SWIR2 + NIR))) +
      (j*((green - SWIR2) / (green + SWIR2))) +
      (k * ((green - NIR) / (green + NIR)))) + (l * SAR)
      
Built up index label
NDBI = (SWIR2 - NIR) / (SWIR2 + NIR)
```
![](https://github.com/ThomasJames/Spectral_Indices/blob/master/Combined.png)





