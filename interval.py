"""
Jonathan Zerez
Spring 2020

Creates intervals that divide image and define sorting boundaries
"""
import numpy as np
import image_utils as util
import pdb

def threshold_interval(im_array, size, lower_thresh, upper_thresh, width=1, func=util.lightness, inverted=False):
    """
    Returns the interval boundaries of the image based on threshold inputs

    Parameters:
        im_array (np.array): An array containing the pixel information for image
        size (tuple): The dimensions of the image
        lower_thresh (float): The lower limit of the threshold
        upper_thresh (float): The upper limit of the threshold
        width (int): The width of intervals in pixels
        func (func): The function to calculate the value for thresholding
        inverted (bool): Toggles whether to use pixels inside or outside of the
                         threhsold values for the interval

    Returns:
        intervals (list): list of lists of lists. Each list contains the
                          beginning and ending pixel index of an interval in a
                          row
    """

    def in_thresh(val):
        """
        determins whether a value is inside or outsie the threshold
        """
        if not inverted:
            return val > lower_thresh and val < upper_thresh
        else:
            return val < lower_thresh or val > upper_thresh


    intervals = []
    for i, y in enumerate(range(0, size[0], width)):
        # Add a list for the current row of the image
        intervals.append([])
        # Keep track if an interval is currently open or not.
        open = in_thresh(func(im_array[y,0]))
        if open:
            intervals[i].append([0])

        # Iterate through all of the pixels in the current row
        for x in range(size[1]):
            level = func(im_array[y,x])
            valid = in_thresh(level)

            # close the interval
            if open and not valid:
                intervals[i][-1].append(x)
                open = False

            # open a new interval
            elif not open and valid:
                intervals[i].append([x])
                open = True
        # Add the last pixel if the last interval in the row is still open
        if open:
            last = x-1
            intervals[i][-1].append(last)
    return intervals

def randomly_filter_interval(intervals, prob):
    """
    randomly eliminate a certain number of intervals, based on a given probability

    Parameters:
        prob: the probability that a given interval is removed from the set

    Returns:
        intervals (list): The filtered intervals
    """
    def roll(prob):
        return np.random.rand() < prob

    # Iterate through all of the intervals
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

    im = Image.open('source/temple.jpg')

    im = util.resize_image(im, 4)
    original_size = im.size
    a = np.asarray(im)


    intervals = threshold_interval(a, np.shape(a), 0.6, 0.75, width=1, func=util.lightness, inverted=True)

    intervals = randomly_filter_interval(intervals, 0.3)
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
