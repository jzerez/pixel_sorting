class Sorter:
    def __init__(self, image_path):
        im = Image.open(image_path)
        self.size = im.size
        self.im = np.asarray(im)

    def calc_dist(self, target_pixel, neighboring_pixels):
        """
        Finds the distance (L2 norm) in RBG space between a target pixel and a list of neighboring pixels
        """
        dists = []
        for pixel in neighboring_pixels:
            dist = np.linalg.norm(np.array(pixel - target_pixel))
            dists.append(dist)
        return dists

    def is_in_frame(self, point, dim):
        """
        Checks to see if a coordinate is within the frame of the image
        """
        return point >= 0 and point < self.size[dim]

    def get_chunk(self, root, queue, seen, dist_func):
        """
        returns a chunk (group) of pixel coordinates that are adjacent to each other and satisfy a specified distance function
        """
        if not queue:
            return seen
        coor = queue.pop()
        if dist_func(root, coor) and coor not in seen:
            seen.add(coor)
            queue.update(self.get_adj(coor))
        return self.get_chunk(root, queue, seen, dist_func)

    def get_adj(self, coor):
        new_adj = []
        for i in [-1, 0, 1]:
            new_x = coor[0] + i
            if self.is_in_frame(new_x, 0):
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    new_y = coor[1] + j
                    if self.is_in_frame(new_y, 1):
                        new_adj.append((new_x, new_y))
        return new_adj



if __name__ == "__main__":
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    im = Image.open('source/IMG_6129.jpg')
    x,y = im.size
    r,g,b = im.split()

    s = Sorter('source/IMG_6129.jpg')
    s.size=(10,10)
    print(s.get_adj((1,1)))
    print(s.get_adj((0,0)))

    def df(root, coor):
        return np.linalg.norm(np.array(root)-np.array(coor)) < 4

    r = (0,0)
    seen = s.get_chunk(r, set([r]), set(), df)
    print(seen)
    plt.figure
    for i in range(len(seen)):
        coor = seen.pop()
        plt.scatter(coor[0], coor[1], color='red')
    plt.xlim((0, 10))
    plt.ylim((0, 10))
    plt.grid()
    plt.show()
