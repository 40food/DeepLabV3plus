# Loading the Colormap
# from scipy.io import loadmat
import numpy as np
#
# colormap = loadmat(
#     "instance-level-human-parsing/instance-level_human_parsing/instance-level_human_parsing/human_colormap.mat"
# )["colormap"]
# colormap = colormap * 100
# colormap = colormap.astype(np.uint8)
#
# print(colormap)

color=[[0,0,0],
 [50,0,0],
 [99,0,0],
 [0,33,0],
 [66,0,19],
 [99,33,0],
 [0,0,33],
 [0,46,86],
 [33,33,0],
 [0,33,33],
 [33,19,0],
 [20,33,50],
 [0,50,0],
 [0,0,99],
 [19,66,86],
 [0,99,99],
 [33,99,66],
 [66,99,33],
 [99,99,0],
 [99,66,0]]

np.save('color.npy', color)
print(np.load('color.npy'))