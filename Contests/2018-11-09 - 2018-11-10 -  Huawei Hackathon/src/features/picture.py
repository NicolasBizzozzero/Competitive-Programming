import math

import numpy as np


def bits_to_picture(bits, picture_height, padding_value=0):
    """ Convert a numpy array of binary values to a graymap picture.
    The width of the picture is computed automaticaly with the `picture_height`
    parameter.
    Missing pixels are completed with the calue of `padding_value`.

    :param bits: The array of bits to convert.
    :param picture_height: The height of the output picture.
    :param padding_value: The value replacing missing pixels.
    """
    # Convert array of bits to array of ints
    bitmap = np.char.mod('%d', bits.reshape(-1, 8))
    bitmap = np.apply_along_axis(lambda b: int("".join(b), 2),
                                 axis=1, arr=bitmap).astype(np.uint8)

    # Convert bitmap vector to a matrix
    number_of_pixels = bitmap.shape[0]
    bitmap.resize(picture_height * math.ceil(bitmap.shape[0] / picture_height))
    bitmap[number_of_pixels:] = padding_value  # Add padding
    picture = bitmap.reshape(picture_height,
                             math.ceil(bitmap.shape[0] / picture_height))
    return picture


def gray_to_rgb(picture):
    """ Convert a grayscale picture represented as a 2D numpy
    array to a RGB picture represented as a 3D numpy array.

    :param picture: The picture to convert.
    """
    return np.stack((picture, ) * 3, axis=-1)


def rgb_to_gray(picture):
    """ Transform a RGB picture to a gray picture. """
    return np.dot(picture[..., :3], [0.299, 0.587, 0.114])


if __name__ == '__main__':
    pass
