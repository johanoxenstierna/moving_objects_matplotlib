
import numpy as np
from matplotlib.pyplot import imread, imsave

THRESHOLD_R = 0.4

cloud = imread('./pics/raw/cloud.png')
cloud_inner = imread('./pics/raw/cloud_inner.png')

array_binary_outer = np.where(cloud[:, :, 0] < THRESHOLD_R, 0.0, 0.1)
array_binary_inner = np.where(cloud_inner[:, :, 0] < THRESHOLD_R, 0.0, 0.9)

cloud[:, :, 3] = array_binary_inner + array_binary_outer

imsave('./pics/processed/cloud.png', cloud)