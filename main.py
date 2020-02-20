image_rotation = -30+180
source = './source/dragon.jpg'
width = 1
from PIL import Image
import numpy as np
import sort
import pdb
import timeit
from sort import sort_pixels
import interval
import image_utils as util

im = Image.open(source)
# im = util.crop_image(im, (500, im.size[0]))
im = util.resize_image(im, 1)
original_size = im.size
im = im.rotate(image_rotation, expand=True)
a = np.asarray(im)

intervals = (interval.threshold_interval(a, np.shape(a), 0.3, 0.6, width=width, func=util.lightness, inverted=True))
intervals = interval.randomly_filter_interval(intervals, 0.5)
# pdb.set_trace()

colors = [np.array([255, 0, 0]), np.array([0, 255, 0]), np.array([0, 0, 255]), np.array([255, 255, 0]), np.array([255, 0, 255]), np.array([0, 255, 255])]

ac = a.copy()

new = sort.sort_pixels(ac, intervals, width=width, sorting_func=util.lightness, reverse=False)
# new = sort.sort_intervals_only(ac, intervals, width=width, sorting_func=util.lightness, reverse=False, prob=0.65)
im2 = Image.fromarray(new)

im2 = im2.rotate(-image_rotation, expand=True)
im2 = util.crop_image(im2, (original_size[1], original_size[0]))
util.test_levels(im2, util.lightness)
im2.show()

print('save image? (Y/N)')
response = input()
if response=='y' or response=='Y':
    print('name the file (with extension)')
    response = input()
    im2.save(response)
