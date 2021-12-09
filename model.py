
import numpy as np

def compute_movement(NUM_FRAMES, pics):
    """returns extent through time"""

    extent_log = np.zeros((NUM_FRAMES, 4))  # left, right, bottom, top borders

    # BOTTOM LEFT POSITION THROUGH TIME ================
    position_vector = np.zeros((NUM_FRAMES, 2))
    v = [0.2, -0.1]

    x_left = 200
    y_bottom = 400

    for i in range(NUM_FRAMES):
        position_vector[i] = [x_left, y_bottom]

        x_left += v[0]
        y_bottom += v[1]

    # SCALING: CLOUD GROWING THROUGH TIME =============
    scale_vector = np.linspace(0.5, 1., NUM_FRAMES)

    extent_log[:, 0] = position_vector[:, 0]  # left border
    extent_log[:, 2] = position_vector[:, 1]  # bottom border

    width = pics['cloud'].shape[1]
    height = pics['cloud'].shape[0]

    for i in range(NUM_FRAMES):  # could be inside above loop whatever

        width_m = width * scale_vector[i]
        height_m = height * scale_vector[i]

        extent_log[i, 1] = position_vector[i, 0] + width_m  # right border
        extent_log[i, 3] = position_vector[i, 1] - height_m  # top border


    return extent_log, scale_vector


def compute_triangles(NUM_FRAMES, pics, extent_log):

    width = pics['cloud'].shape[1]
    height = pics['cloud'].shape[0]

    triangles = []  # not using np since it's nested

    p0 = [0, height]
    p1 = [0 + (width/2), 0]
    p2 = [0 + width, height]

    triangles.append(np.float32([p0, p1, p2]))

    for i in range(1, NUM_FRAMES):
        ext = extent_log[i]
        width = ext[1] - ext[0]  # shoudl maintain data quality since its floating points
        height = ext[2] - ext[3]

        p0 = [ext[0], ext[3] + height]
        p1 = [ext[0] + (width/2), ext[3]]
        p2 = [ext[0] + width, ext[3] + height]

        tri = np.float32([p0, p1, p2])
        triangles.append(tri)

    return triangles
















