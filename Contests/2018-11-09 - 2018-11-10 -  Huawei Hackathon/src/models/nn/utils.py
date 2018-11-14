from functools import partial
from math import floor

import torch
import torch.nn as nn


def conv_architecture(architecture, activation_function, img_size,  max_pool_size=2,
                      padding=1, stride=1, dilation=1, kernel_size=3):
    """Build a compelte convolutionnal architecture.

    Parameters
    ------------
        architecture : list of dict
            Architecture defines how will the convolutionnal part be.
            Each term of the list has to have two items :
            {"filter": nb_filter, "nb_conv": nb_convolutions}

        activation_function : nn.Module
            Activation function between two convolutions

        img_size : tuple of int
            Height, Width and number of channels of the image

        other : @see conv_block

    Returns
    --------
        blocks : list of nn.Module
            The blocks built

        img_size : tuple (h, w)
            The image size (without filters) after the convolutions and the poolings

        img_flatten_size : int
            The size of the vector once image is flatten (it includes the filters of the last layer)

    Example
    --------
        conv_architecture([{"filter": 8, "nb_conv": 2}, {"filter":16, "nb_conv":5}], nn.ReLU, (64, 64, 3))
    """
    blocks = []
    conv_block_parametrized = partial(conv_block, max_pool_size=max_pool_size,
                                      padding=padding, stride=stride, dilation=dilation,
                                      kernel_size=kernel_size, activation_function=activation_function)
    architecture = [{"filter": img_size[-1]}] + architecture
    for prev_block, current_block in zip(architecture, architecture[1:]):
        block, img_size, flatten_size = conv_block_parametrized(prev_block["filter"],
                                            current_block["filter"], current_block["nb_conv"], img_size)

        blocks.extend(block)
    return blocks, img_size, flatten_size


def conv_block(in_filter, output_filter, nb_conv, img_size, max_pool_size=2,
               padding=1, stride=1, dilation=1, kernel_size=3, activation_function=nn.ReLU):
    """Build a list of convolutions with activation_function and adds a maxpool layer.

    Parameters
    ----------
        in_filter :  int
            Number of filters in previous layer

        output_filter :  int
            Number of filters in output layer

        nb_conv : int
            Number of convolution layers stacked before MaxPooling

        activation_function : nn Function
            Activation function after each convolution

    Returns
    ---------
        conv_block : list of nn.Module
            The convolutionnal block with maxpooling

        img_size : (height, width)
            Size of the image

        img_flatten_size : int
            Size of the flattenned image
    """
    nbchannel = in_filter
    nbfilter = output_filter
    conv_block = []

    for i in range(nb_conv):
            conv_block.append(nn.Conv2d(nbchannel, nbfilter, kernel_size, padding=padding, stride=stride, dilation=dilation))
            conv_block.append(activation_function())
            nbchannel = nbfilter  # So all other blocks have the same number of filters
    conv_block.append(nn.MaxPool2d(max_pool_size))

    for i in range(nb_conv):
        h = floor((img_size[0] + 2 * padding - dilation * (kernel_size - 1) - 1) / stride + 1)
        w = floor((img_size[1] + 2 * padding - dilation * (kernel_size - 1) - 1) / stride + 1)
        img_size = (h, w)
    img_size = (img_size[0] / max_pool_size, img_size[1] / max_pool_size)
    img_flatten_size = img_size[0] * img_size[1] * output_filter

    return conv_block, img_size, img_flatten_size


def fc_block(input_size, architecture, activation=nn.ReLU):
    """Build a fully connected block. Last layer has not activation function.

    Parameters
    ----------
        input_size : int
            Size of the input. Don't put it in the architecture

        architecture : list of int
            Each int of the list is the size of the corresponding layer

        activation_function : nn.Module
            Activation function after each layer of the net

    Returns
    ---------
        temp :  list of nn.Module
            The fully connected block without the activation function for the last layer
    """
    temp = []
    architecture = [input_size] + list(architecture)
    for prev_size, next_size in zip(architecture[:-1], architecture[1:]):
         temp.append(nn.Linear(prev_size, next_size))
         temp.append(nn.Dropout(.2)),
         temp.append(activation())
    temp = temp[:-1]  # Remove last activation
    return temp
