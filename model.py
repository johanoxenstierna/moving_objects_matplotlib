import numpy as np

def compute_movement(NUM_FRAMES, pics):
    """returns extent through time"""

    extent_log = np.zeros((NUM_FRAMES, 4))  # left, right, bottom, top borders

    # BOTTOM LEFT POSITION THROUGH TIME =======
    position_vector = np.zeros((NUM_FRAMES, 2))
    v = [0.4, -0.1]  # velocity pixels/frame in x and y

    x_left = 200  # 300
    y_bottom = 400

    for i in range(NUM_FRAMES):

        position_vector[i] = [x_left, y_bottom]

        x_left += v[0]
        y_bottom += v[1]

    # SCALING: CLOUD GROWING THROUGH TIME ======================
    scale_vector = np.linspace(0.5, 1., NUM_FRAMES)

    extent_log[:, 0] = position_vector[:, 0]  # left border
    extent_log[:, 2] = position_vector[:, 1]  # bottom border

    width = pics['cloud'].shape[1]
    height = pics['cloud'].shape[0]

    for i in range(NUM_FRAMES):  # could also be inside above loop whatever
        width_m = width * scale_vector[i]
        height_m = height * scale_vector[i]

        extent_log[i, 1] = position_vector[i, 0] + width_m  # right border
        extent_log[i, 3] = position_vector[i, 1] - height_m  # top border

    return extent_log








    return logger
