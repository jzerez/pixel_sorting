"""
Creates intervals that divide image and define sorting boundaries
"""
import numpy as np
import image_utils as util
import pdb

def threshold(im_array, size, lower_thresh, upper_thresh):
    """
    Divides the image into intervals based on lightness thresholds
    returns: intervals

        -intervals contains `n` lists, where `n` in the number of rows in the image
        -each of the `n` lists contatins `x` lists, where `x` is the number of valid intervals within the row
        -each of the `x` lists contains 2 numbers, the beginning and the end of the interval
    """

    def in_thresh(val):
        """
        returns true if a value is within the specificed threshold
        """
        return val > lower_thresh and val < upper_thresh

    intervals = []
    # iterate through the rows (horizontal)
    for y in range(size[0]):
        intervals.append([])
        # Whether to open a new interval for the first pixel or not
        open = in_thresh(util.lightness(im_array[y,0]))

        if open:
            intervals[y].append([0])

        # Iterate through the pixels in the current row
        for x in range(size[1]):
            level = util.lightness(im_array[y,x])
            valid = in_thresh(level)
            # If the interval is currently open, and the current pixel is not valid, end the current interval
            if open and not valid:
                intervals[y][-1].append(x)
                open = False
            # If there isn't an interval currently open, and the current pixel is valid, open a new interval with the current pixel
            elif not open and valid:
                intervals[y].append([x])
                open = True


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
    intervals = (threshold(a, np.shape(a), 0.3, 0.7))
    colors = [np.array([255, 0, 0]), np.array([0, 255, 0]), np.array([0, 0, 255]), np.array([255, 255, 0]), np.array([255, 0, 255]), np.array([0, 255, 255])]
    pdb.set_trace()
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
