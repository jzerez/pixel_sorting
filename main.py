"""
Jonathan Zerez
Spring 2020

This script is the one that actually performs the pixel sorting
"""
from PIL import Image
import numpy as np
import sort
import pdb
import timeit
from sort import sort_pixels
import interval
import image_utils as util

# Contains image source, rotation information, threshold settings, sorting settings, etc
from parameters import *


# Open image
im = Image.open(source)
# Rotate the image if needed
im = im.rotate(base_rotation, expand=True)
# Resize the image (useful for testing, keep at 1 for final images)
im = util.resize_image(im, resize_factor)
original_size = im.size
im = im.rotate(image_rotation, expand=True)
a = np.asarray(im)

# get intervals
intervals = (interval.threshold_interval(a, np.shape(a), 0.7, 0.91, width=width, func=util.lightness, inverted=True))
intervals = interval.randomly_filter_interval(intervals, 0)

ac = a.copy()

# Sort the pixels
new = sort.sort_pixels(ac, intervals, width=width, sorting_func=util.lightness, reverse=False)
im2 = Image.fromarray(new)

# Unrotate the image
im2 = im2.rotate(-image_rotation, expand=True)
# uncrop added blackspace from the initial rotation
im2 = util.crop_image(im2, (original_size[1], original_size[0]))
im2.show()

print('save image? (Y/N)')
response = input()
if response=='y' or response=='Y':
    print('name the file (with extension)')
    response = input()
    im2.save(response)
im2.close()
