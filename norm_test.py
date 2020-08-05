import numpy as np
import matplotlib.pyplot as plt
from extract import HurricaneExtraction


#npy_file = './Data/NpyData/LIDIA/20172450002.npz'
npy_file = './Data/NpyData/IRMA/20172531622.npz'

data = HurricaneExtraction.read_extraction_data(npy_file)

data = HurricaneExtraction.normalize_using_physics(data)

for d in data:
    fig = plt.figure()
    im = plt.imshow(d, cmap='Greys_r')
    plt.show()
