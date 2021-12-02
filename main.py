
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import model
import utils

# 030
FPS = 20
Writer = animation.writers['ffmpeg']
writer = Writer(fps=FPS, metadata=dict(artist='Me'), bitrate=3600)

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
plt.axis([0, 1280, 720, 0])

pics = utils.load_pics()  # done separately since we might need pics info

im_ax = utils.populate_ax(ax, pics)  # using

NUM_FRAMES = 300
WRITE = 1  # 030

extent_log = model.compute_movement(NUM_FRAMES, pics)

# ============================================


def init():  # Needed for blitting to prevent everything drawn first frame from getting stuck
    return im_ax


def animate(i):

    if i % 10 == 0:  # 030
        print(i)

    cloud_ax = im_ax[0]

    if i == 1:
        cloud_ax.set_alpha(1.0)

    cloud_ax.set_extent(extent_log[i])
    return im_ax


ani = animation.FuncAnimation(fig, animate, frames=NUM_FRAMES, interval=1, blit=True, init_func=init, repeat=False)
# interval=1 usually gonna be slower, check

# 030 with if else
if WRITE == 0:
    plt.show()
else:
    ani.save('./vid.mp4', writer=writer)




