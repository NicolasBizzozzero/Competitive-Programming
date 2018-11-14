import torch
import torh.nn as nn
import torch.optim as optim

from functools import partial

import basics

class AutoEncoder(nn.Module):
    """AutoEncoder generic class.

    """
    def __init__(self, input_size, architecture, activation_function, module_construction_function):
        super(AutoEncoder, self).__init__()
        self.encoder = module_construction_function(architecture, activation_function, input_size)
        self.decoder = module_construction_function(architecture[::-1], activation_function, input_size)

    def forward(self, x):
        encoded = self.encoder(x)
        reconstructed = self.decoder(encoded)
        return encoded, reconstructed


class AutoEncoderFC(AutoEncoder):
    """docstring for AutoEncoderFC."""
    def __init__(self, input_size, architecture, activation_function):
        super(AutoEncoderFC, self).__init__(architecture, activation_function, basics.FullyConnected)


class AutoEncoderConv(AutoEncoder):
    """docstring for AutoEncoderConv."""
    def __init__(self, img_size, architecture, activation_function, parameters):
        convolution_construction = partial(basics.FullyConvolutionnal, **parameters)
        super(AutoEncoderConv, self).__init__(img_size, architecture, activation_function, convolution_construction)
