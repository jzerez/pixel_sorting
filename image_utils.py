import numpy as np
from colorsys import rgb_to_hsv

def calc_dist(self, target_pixel, neighbor):
    """
    Finds the distance (L2 norm) in RBG space between a target pixel and a list of neighboring pixels

    """
    # Get L2 norm
    dist = np.linalg.norm(np.array(pixel - target_pixel))

    # Normalize to 0->1 scale
    normalized_dist = dist / ((3*255**2)**0.5)
    return normalized_dist

def is_in_frame(self, coor):
    """
    Checks to see if a coordinate is within the frame of the image
    """
    return coor[0] >= 0 and coor[0] < self.size[0] and coor[1] >= 0 and coor[1] < self.size[1]

def lightness(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0

if __name__ == "__main__":
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    import pdb
    import timeit
    im = Image.open('source/IMG_6129.jpg')
    a = np.asarray(im)

    x,y = im.size
    r,g,b = im.split()

    s = Sorter('source/IMG_6129.jpg')

    print(s.get_adj((1,1)))
    print(s.get_adj((0,0)))

    def df(root, coor):
        return np.linalg.norm(np.array(root)-np.array(coor)) < 500

    r = (0,0)
    s.get_chunk(r, set([r]), set(), s.get_adj, df)
    print(timeit.timeit(lambda: s.get_chunk(r, set([r]), set(), s.get_adj, df), number=10))

    #
    # print(len(seen))
    # print(s.count)
    # plt.figure
    # for i in range(len(seen)):
    #     coor = seen.pop()
    #     plt.scatter(coor[0], coor[1], color='red')
    # plt.xlim((0, 10))
    # plt.ylim((0, 10))
    # plt.grid()
    # plt.show()
