import os
import numpy as np
from PIL import Image
from netCDF4 import Dataset
from extract import PathSet

root_path = './Data/ABI-L1b-RadC/'
select_date = '2017253'
save_path = './one-day-picture/'

path_set = PathSet(root_path=root_path)
url = path_set.offer_url(select_date=select_date)

while(True):
    try:
        data_list = next(url)
        if len(data_list) <= 0:
            continue
        
        dl = data_list[0]

        g16nc = Dataset(dl[1])
        radiance = g16nc.variables['Rad'][:]
        radiance = (radiance + 25.936) / (804.036 + 25.936)

        img = Image.fromarray(radiance)

        save_name = os.path.join(save_path, dl[0]+'.tiff')
        
        img.save(save_name)

    except StopIteration:
        break
