"""
Creates intervals that divide image and define sorting boundaries
"""
import numpy as np
import image_utils as util
import pdb

def threshold_interval(im_array, size, lower_thresh, upper_thresh, func=util.lightness, inverted=False):
    def in_thresh(val):
        if not inverted:
            return val > lower_thresh and val < upper_thresh
        else:
            return val < lower_thresh or val > upper_thresh
    # pdb.set_trace()
    intervals = []
    for y in range(size[0]):
        intervals.append([])
        open = in_thresh(func(im_array[y,0]))
        if open:
            intervals[y].append([0])

        for x in range(size[1]):
            level = func(im_array[y,x])
            valid = in_thresh(level)
            if open and not valid:
                intervals[y][-1].append(x)
                open = False
            elif not open and valid:
                intervals[y].append([x])
                open = True
    return intervals

def randomly_filter_interval(intervals, prob):
    """
    randomly eliminate a certain number of intervals, based on a given probability
    prob: the probability that a given interval is removed from the set
    """
    def roll(prob):
        return np.random.rand() < prob
    for i, row in enumerate(intervals):
        inds_to_keep = []
        for j, interval in enumerate(row):
            if not roll(prob):
                inds_to_keep.append(j)
        intervals[i] = list(np.array(row)[inds_to_keep])
    return intervals
if __name__ == "__main__":
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    import pdb
    import timeit
    im = Image.open('source/neon.jpeg')
    a = np.asarray(im)
    #
    # checks = 10
    # row_1 = np.array(([True]*checks+[False]*checks)*checks)
    # row_2 = np.array(([False]*checks+[True]*checks)*checks)
    #
    # test_arr = np.vstack([row_1, row_2, row_1, row_2, row_1, row_2, row_1, row_2, row_1, row_2])
    # print(test_arr)
    # im = Image.fromarray(test_arr)
    # im.show()
    # print(np.asarray(im))
    # print(np.shape(test_arr))
    # print(im.size)
    intervals = (threshold_interval(a, np.shape(a), 0.3, 1, inverted=False))
    # colors = [np.array([255, 0, 0]), np.array([0, 255, 0]), np.array([0, 0, 255]), np.array([255, 255, 0]), np.array([255, 0, 255]), np.array([0, 255, 255])]
    colors = [np.array([0,255,0])]
    ac = a.copy()

    for i, row in enumerate(intervals):
        # pdb.set_trace()
        for interval in row:
            if len(interval) > 1:
                try:
                    ac[i][interval[0]:interval[1]] = colors[i % len(colors)] * np.ones([interval[1] - interval[0], 1])
                except IndexError:
                    pdb.set_trace()
    pdb.set_trace()
    im2 = Image.fromarray(ac)
    im2.show()
