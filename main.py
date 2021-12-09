import matplotlib.pyplot as plt
import matplotlib.animation as animation
import utils
import model
import time

# affine mpl ====
# import matplotlib.transforms as mtransforms
# import numpy as np

# affine cv2 ====
import cv2

FPS = 20

WRITE = 0
Writer = animation.writers['ffmpeg']
writer = Writer(fps=FPS, metadata=dict(artist='Me'), bitrate=3600)


fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
plt.axis([0, 1280, 720, 0])

NUM_FRAMES = 300

pics = utils.load_pics()
# pics['cloud'] = np.flipud(pics['cloud'])
im_ax = utils.populate_ax(ax, pics)

extent_log, scale_vector = model.compute_movement(NUM_FRAMES, pics)
triangles = model.compute_triangles(NUM_FRAMES, pics, extent_log)
aa = 6

def init():
    return im_ax


def animate(i):

    if i % 10 == 0:
        print(i)

    # cloud_ax = im_ax[0]
    # if i == 1:
    #     cloud_ax.set_alpha(1.)

    #SET EXTENT ====================
    # cloud_ax.set_extent(extent_log[i])


    # AFFINE TRANSFORM MPL =========

    # shift_x = 200 + extent_log[i, 0] - extent_log[0, 0]
    # shift_y = 250 + extent_log[0, 2] - extent_log[i, 2]
    # M = mtransforms.Affine2D().scale(scale_vector[i], scale_vector[i]).translate(shift_x, shift_y)
    # cloud_ax.set_transform(M)

    # AFFINE TRANSFORM CV2 =========
    time0 = time.time()
    t0 = triangles[0]
    t1 = triangles[i]

    im_ax['cloud'].remove()
    M = cv2.getAffineTransform(t0, t1)
    dst = cv2.warpAffine(pics['cloud'], M, (650, 400))

    im_ax['cloud'] = ax.imshow(dst, zorder=1, alpha=0.8)
    print(time.time() - time0)

    return im_ax

ani = animation.FuncAnimation(fig, animate,
                              # blit=True, interval=50, init_func=init,
                              frames=NUM_FRAMES, repeat=False)

if WRITE == 0:
    plt.show()
else:
    ani.save('./vid.mp4', writer=writer)