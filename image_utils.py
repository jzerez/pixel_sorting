import numpy as np
from colorsys import rgb_to_hsv
class Sorter:
    def __init__(self, image_path):
        im = Image.open(image_path)
        self.size = im.size
        self.im = np.asarray(im)
        self.count = 0

    def calc_dist(self, target_pixel, neighboring_pixels):
        """
        Finds the distance (L2 norm) in RBG space between a target pixel and a list of neighboring pixels
        """
        dists = []
        for pixel in neighboring_pixels:
            dist = np.linalg.norm(np.array(pixel - target_pixel))
            dists.append(dist)
        return dists

    def is_in_frame(self, coor):
        """
        Checks to see if a coordinate is within the frame of the image
        """
        return coor[0] >= 0 and coor[0] < self.size[0] and coor[1] >= 0 and coor[1] < self.size[1]

    def get_chunk(self, root, queue, seen, adj_func, filter_func):
        """
        returns a chunk (group) of pixel coordinates that are adjacent to each other and satisfy a specified filter function:

        what qualifies as adjacent is determined by the adj_func
        what qualifies as acceptable is determined by the filter_func
        """
        while queue:
            self.count += 1
            coor = queue.pop()
            if filter_func(root, coor) and coor not in seen:
                seen.add(coor)
                adj = [adj for adj in adj_func(coor) if adj not in seen]
                queue.update(adj)
        return seen

    # def threshold(self, lower_thresh, upper_thresh)


    def get_adj(self, coor):
        """
        return the up to eight adjacent coordinates to a given coordinate
        """
        new_adj = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                new_coor = (coor[0] + i, coor[1] + j)

                if self.is_in_frame(new_coor):
                    new_adj.append(new_coor)
        return new_adj

    def get_horiz_neighbors(self,coor):
        """
        return the up to two horizontal neighbors to a given coordinate
        """
        neighbors = []
        for i in [-1, 1]:
            new_coor = (coor[0]+i, coor[1])
            if self.is_in_frame(new_coor):
                neighbors.append(new_coor)
        return neighbors

    def get_vert_neighbors(self,coor):
        """
        return the up to two vertical neighbors to a given coordinate
        """
        neighbors = []
        for j in [-1, 1]:
            new_coor = (coor[0], coor[1]+j)
            if self.is_in_frame(new_coor):
                neighbors.append(new_coor)
        return neighbors

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
