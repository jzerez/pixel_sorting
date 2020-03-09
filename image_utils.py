"""
Jonathan Zerez
Spring 2020

This script provides functionality for evaluating aspects of input images
"""

import numpy as np
from colorsys import rgb_to_hsv
import pdb

def calc_dist(target_pixel, neighbor):
    """
    Finds the distance (L2 norm) in color space between a target pixel and a
    neighboring pixel

    Parameters:
        target_pixel (iterable): contains the RGB/HSV values of a pixel
        neighbor (iterable): contains the RGB/HSV values of the neighbor pixel

    Returns:
        normalized_dist (float): A float from [0, 1], the distance between the
                                 pixels
    """
    # Get L2 norm
    dist = np.linalg.norm(np.array(pixel - target_pixel))

    # Normalize to 0->1 scale
    normalized_dist = dist / ((3*255**2)**0.5)
    return normalized_dist

def is_in_frame(coor):
    """
    Checks to see if a coordinate is within the frame of the image

    Parameters:
        coor (tuple): The x,y coordinates to check. Origin is at the upper left

    Returns:
        (bool): if the coordinate is in the frame or not
    """
    return coor[0] >= 0 and coor[0] < self.size[0] and coor[1] >= 0 and coor[1] < self.size[1]

def lightness(pixel):
    """
    Returns the intensity or lightness of a given pixel from [0,1]
    """
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0

def hue(pixel):
    """
    Returns the hue value of a given pixel from [0,1]
    """
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[0]

def saturation(pixel):
    """
    Returns the saturation value of a given pixel from [0,1]
    """
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[1]

def crop_image(image, dimensions):
    """
    Crops the image to specified dimensions. Crop is centered on the image
    center

    Parameters:
        image (Image): the image to crop
        dimensions (tuple): the final dimensions to crop the image to [width, height]

    Returns:
        (Image): the cropped image
    """

    original_size = image.size
    side_width = dimensions[1]/2
    top_length = dimensions[0]/2
    # find the center of the image to center the crop
    center = [dim/2 for dim in original_size]

    # define the corners of the image
    left = int(center[0]-side_width)
    upper = int(center[1]-top_length)
    right = int(center[0]+side_width)
    lower = int(center[1]+top_length)

    frame = (left, upper, right, lower)
    return image.crop(box=frame)



def test_levels(image, value_func):
    """
    Used to evaluate pixel values of the entire image ex: lightness, satruation
    This is useful for determining good threshold values to use for sorting

    Parameters:
        image (Image): The image to evaluate
        value_func (func): the value of pixels to calculate and displace
    """
    import matplotlib.pyplot as plt
    a = np.asarray(image)

    size = a.shape[0:2]

    # Get the values for each pixel
    levels = np.zeros(size)
    for y in range(size[0]):
        for x in range(size[1]):
            levels[y, x] = value_func(a[y, x])

    # plot the values as heatmaps
    plt.figure()
    f = plt.imshow(levels, aspect='auto')
    plt.colorbar(f)
    if value_func == saturation:
        plt.title('Saturation of Image')
    elif value_func == hue:
        plt.title('Hue of Image')
    elif value_func == lightness:
        plt.title('lightness of Image')
    plt.show()


def resize_image(image, factor):
    """
    Resizes the image (maintains aspect ratio)

    Parameters:
        image (Image): image to resize
        factor (int): The factor to shrink both dimensinos of the image by

    Returns:
        (Image): the resized image
    """
    original_size = image.size
    return image.resize((original_size[0] // factor, original_size[1] // factor))

if __name__ == "__main__":
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    import pdb
    import timeit

    from parameters import *

    im = Image.open(source)

    im = resize_image(im, 5)
    size = im.size

    print(im.size)
    test_levels(im, interval_func)
