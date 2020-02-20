import numpy as np
from colorsys import rgb_to_hsv
import pdb

def calc_dist(target_pixel, neighbor):
    """
    Finds the distance (L2 norm) in RBG space between a target pixel and a list of neighboring pixels

    """
    # Get L2 norm
    dist = np.linalg.norm(np.array(pixel - target_pixel))

    # Normalize to 0->1 scale
    normalized_dist = dist / ((3*255**2)**0.5)
    return normalized_dist

def is_in_frame(coor):
    """
    Checks to see if a coordinate is within the frame of the image
    """
    return coor[0] >= 0 and coor[0] < self.size[0] and coor[1] >= 0 and coor[1] < self.size[1]

def lightness(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0

def crop_image(image, dimensions):
    original_size = image.size
    side_width = dimensions[1]/2
    top_length = dimensions[0]/2
    center = [dim/2 for dim in original_size]
    left = int(center[0]-side_width)
    upper = int(center[1]-top_length)
    right = int(center[0]+side_width)
    lower = int(center[1]+top_length)

    frame = (left, upper, right, lower)
    return image.crop(box=frame)

def hue(pixel):
    # pdb.set_trace()
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[0]

def saturation(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[1]

def test_levels(image, value_func):
    import matplotlib.pyplot as plt
    a = np.asarray(image)

    size = a.shape[0:2]

    levels = np.zeros(size)
    for y in range(size[0]):
        for x in range(size[1]):
            levels[y, x] = value_func(a[y, x])
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
    original_size = image.size
    return image.resize((original_size[0] // factor, original_size[1] // factor))

if __name__ == "__main__":
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    import pdb
    import timeit
    im = Image.open('helpme.jpg')

    # ac = np.zeros()
    # imm = crop_image(im, [400, 400])
    # imm.show()
    im = resize_image(im, 1)
    size = im.size

    print(im.size)
    test_levels(im, lightness)
    # test_levels(im, hue)
    # test_levels(im, saturation)
