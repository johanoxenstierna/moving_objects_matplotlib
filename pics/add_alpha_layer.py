"""Adds transparency layer to pics"""

import os
import numpy as np
from matplotlib.pyplot import imread, imsave

THRESHOLD_R = 0.4

cloud = imread('./pics/raw/cloud.png')
cloud_inner = imread('./pics/raw/cloud_inner.png')

array_binary_outer = np.where(cloud[:, :, 0] < THRESHOLD_R, 0.0, 0.5)  # where alpha should be 1, and 0 otherwise
array_binary_inner = np.where(cloud_inner[:, :, 0] < THRESHOLD_R, 0.0, 0.5)  # where alpha should be 1, and 0 otherwise
cloud[:, :, 3] = array_binary_inner + array_binary_outer

imsave('./pics/processed/cloud.png', cloud)

aa = 5


