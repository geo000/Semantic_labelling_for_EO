from sentinelhub import WmsRequest, MimeType, CRS, BBox, SHConfig, DataSource
from sentinelhub import SHConfig
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox
import matplotlib.pyplot as plt
from sentinelhub import DataSource
from datetime import timedelta, date
import numpy as np
from sentinelhub import CustomUrlParam

"""

__________________________________
data_type
Specify what type of data you need
DEM = 'DEM'
radar = "BANDS-S1-IW"
multipectral = 'BANDS-S2-L1C'
BandsS2cloudless = 'BANDS-S2CLOUDLESS'


__________________________________   
bbox
Specify the bounding box in the format and the CRS:
EG:
betsiboka_coords_wgs84 = [46.16, -16.15, 46.51, -15.58]
betsiboka_bbox = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)

__________________________________       
date
To pull down one image, use a single date in the format:
'2017-12-20'
for the most recent image use 'latest'

To pull down images within a specific date range, use the date_range function. 
Arguments should take be datetime 
start_date = date(2017, 1, 1)        
end_date = date(2020, 3, 1)       
   
__________________________________   
width
Specify the width in pixels

__________________________________   
height
Specify the height in pixels

__________________________________   
maxcc
Specify the maximum cloud cover in percentage.
eg 0% cloud cover = maxcc=0.0
__________________________________   
config
Account configuration to access sentinel hub. 
https://www.sentinel-hub.com/

__________________________________   
"""

class Sentinel_request:
    def __init__(self, data_type=None, bbox=None, date=None, width=None,
                       height=None, maxcc=None, config=None, start_date=None,
                       end_date=None):

        self.data_type = data_type
        self.bbox = bbox
        self.date = date
        self.width = width
        self.height = height
        self.maxcc = maxcc
        self.config = config
        self.start_date = start_date
        self.end_date = end_date

    def request_batch(self):
        for i in range(len(self.date)):
            data = (self.request_single(self.data_type,
                                        self.bbox,
                                        self.date[i],
                                        self.width,
                                        self.height,
                                        self.maxcc,
                                        self.config).get_data())
            try:
                data = np.array(data[-1])
                plt.imsave(str(self.date_list[i]) + ".png", data)
            except:
                pass

    def request_single(self):
        image = WmsRequest(
            layer=self.data_type,
            bbox=self.bbox,
            time=self.date,
            width=self.width,
            height=self.height,
            maxcc=self.maxcc,
            image_format=MimeType.TIFF_d32f,
            config=self.config).get_data()
        return image

    def date_range(self):
        for n in range(int((self.end_date - self.start_date).days)):
            yield self.start_date + timedelta(n)


if __name__ == "__main__":

    # Get the configuration
    INSTANCE_ID = '77763d50-1c52-42a9-8850-2a84823362ce'
    if INSTANCE_ID:
        config = SHConfig()
        config.instance_id = INSTANCE_ID
    else:
        config = None

    # Create bounding box with CRS assigned
    betsiboka_coords_wgs84 = [46.16, -16.15, 46.51, -15.58]
    betsiboka_bbox = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)

    #
    S2_data_request = Sentinel_request(data_type="BANDS-S2-L1C",
                            bbox=betsiboka_bbox,
                            date="latest",
                            width=315,
                            height=512,
                            maxcc=0.0,
                            config=config)

    # request the single image
    S2_data = S2_data_request.request_single()

    # Identify band of interest
    B01 = 0

    # Extract the band of interest
    single_image = np.array(S2_data[-1][:, :, B01])

    # Create list containing all dates with a specified range
    start_date = date(2017, 1, 1)
    end_date = date(2019, 3, 1)
    date_list = []
    for single_date in Sentinel_request.date_range(start_date=start_date, end_date=end_date):
        date_list.append(str(single_date.strftime("%Y-%m-%d")))

    print(date_list)
