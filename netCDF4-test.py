from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import os

path = 'D:\\Code\\TyphoonExtraction\\Data\\ABI-L1b-RadC\\M3C07\\2017253\\'
#name = 'OR_ABI-L1b-RadC-M3C01_G16_s20172450002151_e20172450004524_c20172450004569.nc'
name = 'OR_ABI-L1b-RadC-M3C07_G16_s20172531622165_e20172531624549_c20172531624583.nc'

# names = sorted(os.listdir(path))
# for name in names:
#     g16nc = Dataset(path+name, 'r')
#     #print(g16nc.variables.keys())
#     radiance = g16nc.variables['Rad'][:]
#     radiance = (radiance + 25.936) / (804.036 + 25.936)
#     #print(type(radiance))
#     g16nc.close()
#     g16nc = None

#     #Initail Radiance 辐射亮度
#     fig = plt.figure(figsize=(8,8),dpi=200)
#     im = plt.imshow(radiance, cmap='Greys_r')
#     cb = fig.colorbar(im, orientation='horizontal')
#     cb.set_ticks([1, 100, 200, 300, 400, 500, 600])
#     cb.set_label('Radiance (W m-2 sr-1 um-1)')
#     plt.show()

a = np.zeros(shape=(2,2))
print(type(a))


g16nc = Dataset(path+name, 'r')
#print(g16nc.variables.keys())

nadir = g16nc.variables['geospatial_lat_lon_extent'].geospatial_lon_nadir
print(nadir)

yimage_bound = g16nc.variables['y_image_bounds'][:]
print(yimage_bound)

radiance = g16nc.variables['Rad'][:]
#radiance = (radiance + 25.936) / (804.036 + 25.936)
#radiance = (radiance + 0.0376) / (25.290 + 0.0376)
print(type(radiance))

y = g16nc.variables['y'][:]
print(y)

x = g16nc.variables['x'][:]
print(x)

g16nc.close()
g16nc = None

#Initail Radiance 辐射亮度
fig = plt.figure(figsize=(8,8),dpi=200)
im = plt.imshow(radiance, cmap='Greys_r')
cb = fig.colorbar(im, orientation='horizontal')
cb.set_ticks([1, 100, 200, 300, 400, 500, 600])
cb.set_label('Radiance (W m-2 sr-1 um-1)')
plt.show()


# # Reflectance 反射比
# # Define some constants needed for the conversion. From the pdf linked above
# Esun_Ch_01 = 726.721072
# Esun_Ch_02 = 663.274497
# Esun_Ch_03 = 441.868715
# d2 = 0.3

# # Apply the formula to convert radiance to reflectance
# ref = (radiance * np.pi * d2) / Esun_Ch_02

# # Make sure all data is in the valid data range
# ref = np.maximum(ref, 0.0)
# ref = np.minimum(ref, 1.0)

# # Plot reflectance
# fig = plt.figure(figsize=(6,6),dpi=200)
# im = plt.imshow(ref, vmin=0.0, vmax=1.0, cmap='Greys_r')
# cb = fig.colorbar(im, orientation='horizontal')
# cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
# cb.set_label('Reflectance')
# plt.show()