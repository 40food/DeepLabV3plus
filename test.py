import numpy as np
from scipy.io import loadmat

colors=np.load('Pole_color.npy')
print(colors)

# Loading the Colormap
colormap = loadmat(
    "instance-level-human-parsing/instance-level_human_parsing/instance-level_human_parsing/human_colormap.mat"
)["colormap"]
colormap = colormap * 100
colormap = colormap.astype(np.uint8)
print(colormap)