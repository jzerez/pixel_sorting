import image_utils as util

def sort_pixels(im_array, intervals, min_interval=2, sorting_func=util.lightness, reverse=False):
    for i, row in enumerate(intervals):
        for interval in row:
            if len(interval) > 1:
                if interval[1] - interval[0] > min_interval:
                    pixels = im_array[i][interval[0]:interval[1]]
                    # pdb.set_trace()
                    ordered_pixels = sorted(pixels, key=lambda pix: sorting_func(pix), reverse=reverse)
                    im_array[i][interval[0]:interval[1]] = ordered_pixels
    return im_array

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

    new = sort_pixels(ac, ac.shape, intervals)
    im2 = Image.fromarray(new)
    im2.show()
