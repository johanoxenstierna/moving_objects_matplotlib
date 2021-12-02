from matplotlib.pyplot import imread

def load_pics():
    pics = {}
    pics["background"] = imread('./pics/raw/background.png')  # 482, 187
    pics["cloud"] = imread('./pics/processed/cloud.png')  # 482, 187

    return pics

def populate_ax(ax, pics):
    # im_ax = {}  # OBS doesn't work with blitting
    im_ax = []

    _ = ax.imshow(pics['background'], zorder=1, alpha=0.9)  # not going to animate backgr

    cloud_ax = ax.imshow(pics['cloud'], zorder=2, alpha=0.)
    im_ax.append(cloud_ax)

    return im_ax

