"""
Jonathan Zerez
Spring 2020

Use to define parameters to carry out pixel sorting
"""
import image_utils as util

# angle (degrees) the intervals will be sorted in
image_rotation = -90
# used to rotate the image in case it imports incorrectly
base_rotation = 0
# image source
source = './source/taipei/fake_temple.jpg'
# width of the intervals in pixels
width = 5
# how much to downscale the image (preserves aspect ratio)
resize_factor = 10
# If True, pixels will be added to the interval if they out outside the threshold
inverted_interval = True
# function for determining the intervals
interval_func = util.lightness
# The threshold limits
lower_thresh = 0.7
upper_thresh = 0.91
# The function for sorting intervals
sorting_func = util.lightness
# Probability that intervals don't get sorted
interval_probability = 0
