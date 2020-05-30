import math                       
import numpy as np                
import matplotlib.pyplot as plt   
                                  
"""                                                                             
dim_pix - Dimensions of the target image (Model input)                          
im - 2D numpy array to be split                                                 
Location - A string to save the location of the image                           
dytpe - String to describe (Label or input)                                     
"""                                                                             
                                                                                
def split_image(dim_pix, im, location, dtype):                                  
    rows = []                                                                   
    for i in range((math.floor(im.shape[0] / dim_pix))):                        
        rows.append(i)                                                          
    print("Rows", rows)                                                         
                                                                                
    columns = []                                                                
    for i in range((math.floor(im.shape[1] / dim_pix))):                        
        columns.append(i)                                                       
    print("columns", columns)                                                   
                                                                                
    a = 0                                                                       
    for i in rows:                                                              
        for j in columns:                                                       
            plt.imsave(f"Data/{a}{dtype}{location}.png",                        
                       im[0 + (dim_pix * j): dim_pix + (dim_pix * j),           
                       0 + dim_pix * i: dim_pix + (dim_pix * i)])               
            a += 1                                                              
                                                                                
split_image(dim_pix=244, im=COM, location="Shanghaiiii", dtype="Label")         
                                                                                
