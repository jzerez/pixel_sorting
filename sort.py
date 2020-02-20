import image_utils as util
import pdb
import matplotlib.pyplot as plt
import numpy as np
def sort_pixels(im_array, intervals, width, min_interval=2, sorting_func=util.lightness, reverse=False):

    for i, row in enumerate(intervals):
        for interval in row:
            if len(interval) > 1:
                if interval[1] - interval[0] > min_interval:
                    curr_row = i * width
                    pixels = im_array[curr_row][interval[0]:interval[1]]
                    ordered_pixels = np.array(sorted(pixels, key=lambda pix: sorting_func(pix), reverse=reverse))

                    for j in range(width):
                        if curr_row + j < len(intervals):
                            im_array[curr_row+j][interval[0]:interval[1]] = ordered_pixels
    return im_array

def sort_intervals_only(im_array, intervals, width, min_interval=2, sorting_func=util.lightness, reverse=False, prob=0):
    im_copy = np.zeros(im_array.shape, dtype=np.uint8)
    for i, row in enumerate(intervals):
        curr_row = i * width
        for interval in row:
            pixels = im_array[curr_row][interval[0]:interval[1]]
            if np.random.random() < prob:
                for j in range(width):
                    if curr_row + j < len(intervals):
                        im_copy[curr_row+j][interval[0]:interval[1]] = pixels
            elif len(interval) > 1:
                if interval[1] - interval[0] > min_interval:
                    ordered_pixels = np.array(sorted(pixels, key=lambda pix: sorting_func(pix), reverse=reverse))

                    for j in range(width):
                        if curr_row + j < len(intervals):
                            im_copy[curr_row+j][interval[0]:interval[1]] = ordered_pixels

    plt.figure()
    plt.imshow(im_copy, aspect='auto')
    plt.show()

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
