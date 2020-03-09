# Pixel Sorting
This is an art project that allows you to create glitchy looking images through pixel sorting. In pixel sorting, you first iterate through the image, and identify intervals of pixels that fall within a certain threshold for some value (ex: pixel intensity or hue). Afterwards, you sort the pixels within each interval by some criteria (ex: pixel intensity or saturation). If the correct threshold values are chosen, you can make some pretty cool images, like this!

![cherry_blossom.jpg before and after](./examples/cherry_blossom_comparison.jpg =800x)
![fake_temple.jpg before and after](./examples/fake_temple_comparison.jpg =800x)

## Installation
Install the dependencies before using:
`pip install --requirement requirements.txt`

## How to use
You can edit the pixel sorting parameters in `parameters.py`. I suggest that you test different parameters using a downsized version of the image first (`resize_factor = 6`). This will allow you to see what the parameters to do the image a lot faster, and will save you a lot of time. When you are satisfied, you can run the program on the original image.

## General Tips
* Sorting by lightness usually is the way to go
* You should generally keep the function for determining intervals and the function for sorting the same (ie: use hue for both, don't use hue for one and saturation for another)
* Increasing the width of intervals can make the pixelated effect more apparent, which is a good thing. It also decreases run time proportionally!
* Running `image_utils.py` will execute the `test_levels()` function on your chosen source image, and this will allow you to better understand how to choose threshold values
