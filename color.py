#예측에 사용할 컬러맵을 만드는 코드

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
 [99,0,0],
 [0,99,0],
 [0,0,99],
 [99,99,0],
 [99,0,99]]

np.save('Pole_color.npy', color)
print(np.load('Pole_color.npy'))