image_rotation = 65
source = './source/temple.jpg'
width = 5
from PIL import Image
import numpy as np
import sort
import pdb
import timeit
from sort import sort_pixels
import interval
import image_utils as util

im = Image.open(source)
im = util.resize_image(im, 1)
original_size = im.size
im = im.rotate(image_rotation, expand=True)
a = np.asarray(im)

intervals = (interval.threshold_interval(a, np.shape(a), 0.65, 0.75, width=width, func=util.lightness, inverted=True))

intervals = interval.randomly_filter_interval(intervals, 0.1)
colors = [np.array([255, 0, 0]), np.array([0, 255, 0]), np.array([0, 0, 255]), np.array([255, 255, 0]), np.array([255, 0, 255]), np.array([0, 255, 255])]

ac = a.copy()

new = sort_pixels(ac, intervals, width=width, sorting_func=util.saturation, reverse=False)
im2 = Image.fromarray(new)
# pdb.set_trace()
im2 = im2.rotate(-image_rotation, expand=True)
im2 = util.crop_image(im2, (original_size[1], original_size[0]))
im2.show()
