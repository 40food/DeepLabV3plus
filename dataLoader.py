import os
from glob import glob
import numpy as np
import cv2

DATA_DIR = "pole_data"
# NUM_TRAIN_START = 1401
NUM_TRAIN_IMAGES = 1500
# NUM_VAL_START = 1601
NUM_VAL_IMAGES = 500

train_masks = sorted(glob(os.path.join(DATA_DIR, "Train/SegmentationClass/*")))[
              1390:NUM_TRAIN_IMAGES]
val_masks = sorted(glob(os.path.join(DATA_DIR, "Train/SegmentationClass/*")))[
              NUM_TRAIN_IMAGES:NUM_TRAIN_IMAGES+NUM_VAL_IMAGES]
# val_masks = sorted(glob(os.path.join(DATA_DIR, "Val/SegmentationClass/*")))[
#             :NUM_VAL_IMAGES]

def load_image(filepath):
    img = cv2.imread(filepath)
    if img is None:
        raise ValueError(f"Image not found or unable to load: {filepath}")
    return img

# color=[[0,0,0],
#  [150,162,4],
#  [143,22,98],
#  [51,221,255],
#  [201,53,198],
#  [250,50,83]]

cmap = {(0, 0, 0): 0, (150, 162, 4): 1, (143, 22, 98): 2,
        (51, 221, 255): 3, (201, 53, 198): 4, (250, 50, 83): 5}
def rgb2mask(img):
    filepath=img
    img=load_image(img)
    assert len(img.shape) == 3
    height, width, ch = img.shape
    assert ch == 3

    W = np.power(256, [[0],[1],[2]])

    img_id = img.dot(W).squeeze(-1)
    values = np.unique(img_id)

    mask = np.zeros(img_id.shape)
    cv2.imwrite("pole_data/Train/Mask/" + os.path.basename(filepath), mask)
    for c in enumerate(values):
        try:
            mask[img_id==c] = cmap[tuple(img[img_id==c][0])]
        except:
            pass
    return mask

def rgb2mask2(img):
    filepath=img
    img=load_image(img)
    assert len(img.shape) == 3
    height, width, ch = img.shape
    assert ch == 3

    W = np.power(256, [[0],[1],[2]])

    img_id = img.dot(W).squeeze(-1)
    values = np.unique(img_id)

    mask = np.zeros(img_id.shape)
    cv2.imwrite("pole_data/Val/Mask/" + os.path.basename(filepath), mask)
    for c in enumerate(values):
        try:
            mask[img_id==c] = cmap[tuple(img[img_id==c][0])]
        except:
            pass
    return mask

# mask=list(map(rgb2mask,train_masks))
mask=list(map(rgb2mask,val_masks))
# mask2=list(map(rgb2mask2,val_masks))