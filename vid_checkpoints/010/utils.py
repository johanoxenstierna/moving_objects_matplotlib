from matplotlib.pyplot import imread

def load_pics():
    pics = {}
    pics["background"] = imread('./pics/background.png')  # 482, 187
    return pics


def populate_ax(ax):
    im_ax = {}
    pics = load_pics()

    im_ax['background'] = ax.imshow(pics['background'], zorder=1, alpha=1)

    return ax


def generate_transparency():
    pass
