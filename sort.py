"""
Jonathan Zerez
Spring 2020

This script provides utilities for taking intervals of pixels and sorting them
based on given rules and parameters
"""

import image_utils as util
import pdb
import matplotlib.pyplot as plt
import numpy as np

def sort_pixels(im_array, intervals, width, min_interval=2, sorting_func=util.lightness, reverse=False):
    """
    Takes intervals of pixels, sorts them, and replaces the pixels in the image
    accordingly

    Parameters:
        im_array (np.array): The array containing the pixels of the image
        intervals (list): A list of lists that contain the beginning and ending
            index for each interval for each row of the image
        width (int): The number pixels of each interval's width
        min_interval (int): The minimum number of pixels that need to be
            contained in an interval to be considered for sorting
        sorting_func (func): The criteria to sort by
        reverse (bool): Toggle forward or reverse sorting

    Returns:
        im_array (np.array): The array with sorted pixels
    """

    for i, row in enumerate(intervals):
        for interval in row:
            # Ensure the interval isn't empty
            # ie: make sure it has both a starting and ending index
            if len(interval) > 1:
                if interval[1] - interval[0] > min_interval:
                    curr_row = i * width
                    # Get pixels associated with the interval
                    pixels = im_array[curr_row][interval[0]:interval[1]]
                    # sort the pixels
                    ordered_pixels = np.array(sorted(pixels, key=lambda pix: sorting_func(pix), reverse=reverse))

                    # Replace the pixels in the im_array with the sorted pixels
                    for j in range(width):
                        # Make sure that the pixels will fit into the image
                        if curr_row + j < im_array.shape[0]:
                            im_array[curr_row+j][interval[0]:interval[1]] = ordered_pixels
    return im_array

def sort_intervals_only(im_array, intervals, width, min_interval=2, sorting_func=util.lightness, reverse=False, prob=0):
    """
    Takes intervals of pixels, sorts them, and replaces the pixels in the image
    accordingly. Pixels not contained in intervals are blacked out

    Parameters:
        im_array (np.array): The array containing the pixels of the image
        intervals (list): A list of lists that contain the beginning and ending
                          index for each interval for each row of the image
        width (int): The number pixels of each interval's width
        min_interval (int): The minimum number of pixels that need to be
                            contained in an interval to be considered for sorting
        sorting_func (func): The criteria to sort by
        reverse (bool): Toggle forward or reverse sorting
        prob (float): The probability that an interval just gets copied without
                      being sorted

    Returns:
        im_copy (np.array): an array that contains only the sorted pixels.
            Pixels not contained in intervals are black
    """

    # Initialize black image copy
    im_copy = np.zeros(im_array.shape, dtype=np.uint8)
    for i, row in enumerate(intervals):
        curr_row = i * width
        for interval in row:
            # Get pixels in the interval
            pixels = im_array[curr_row][interval[0]:interval[1]]

            if np.random.random() < prob:
                # Just copy the pixels without sorting
                for j in range(width):
                    if curr_row + j < len(intervals):
                        im_copy[curr_row+j][interval[0]:interval[1]] = pixels
            elif len(interval) > 1:
                if interval[1] - interval[0] > min_interval:
                    ordered_pixels = np.array(sorted(pixels, key=lambda pix: sorting_func(pix), reverse=reverse))

                    for j in range(width):
                        if curr_row + j < len(intervals):
                            im_copy[curr_row+j][interval[0]:interval[1]] = ordered_pixels

    return im_copy


if __name__ == "__main__":
    from PIL import Image
    import numpy as np
    import interval
    import pdb
    import timeit
    im = Image.open('source/neon.jpeg')
    a = np.asarray(im)

    intervals = (interval.threshold_interval(a, np.shape(a), 0.3, 0.7))
    colors = [np.array([255, 0, 0]), np.array([0, 255, 0]), np.array([0, 0, 255]), np.array([255, 255, 0]), np.array([255, 0, 255]), np.array([0, 255, 255])]

    ac = a.copy()

    new = sort_pixels(ac, intervals, width=1)
    im2 = Image.fromarray(new)
    im2.show()
