import torch
import torch.nn as nn

import utils

class FullyConnected(nn.Module):
    """This is a class to make the creation of fully connected block easier.

    Attributes
    -----------
        fc : nn.Module
            The fully connected block
    """
    def __init__(self, input_size, architecture, activation_function=nn.ReLU):
        """Instantiate a FullyConnected object

        Parameters
        -----------
            input_size : int
                Size of the input. Don't put it in the architecture

            architecture : list of int
                Each int of the list is the size of the corresponding layer

            activation_function : nn.Module, optionnal
                Activation function after each layer of the net. Default is nn.ReLU

        """
        super(FullyConnected, self).__init__()
        block = utils.fc_block(input_size, architecture)
        self.fc = nn.Sequential(*block)

    def forward(self, x):
        return self.fc(x)


class FullyConvolutionnal(nn.Module):
    """This is a class to make the creation of fully convolutionnal block easier.

    Note
    ----------
        For now, convolutionnal blocks are convolutions and max poolings

    Attributes
    -----------
        conv : nn.Module
            The convolution-pooling block

        flattenned_size : int
            Size of the output after the convolutions and maxpoolings
    """
    def __init__(self, architecture, activation_function, img_size, **kwargs):
        """Instantiate a FullyConvolutionnal object.

        Parameters
        ------------
            architecture : list of dict
                Architecture defines how will the convolutionnal part be.
                Each term of the list has to have two items :
                {"filter": nb_filter, "nb_conv": nb_convolutions}.
                See utils.conv_architecture for an example

            activation_function : nn.Module
                Activation function between two convolutions

            img_size : tuple of int
                Height, Width and number of channels of the image

            **kwargs : dict
                This is given to utils.conv_architecture

        """
        super(FullyConvolutionnal, self).__init__()
        blocks, img_size, img_flatten_size = utils.conv_architecture(architecture,
                            activation_function, img_size, **kwargs)

        self.conv = nn.Sequential(*blocks)
        self.flattenned_size = int(img_flatten_size)

    def forward(self, x):
        return self.conv(x)


class ConvNet(nn.Module):
    """This class is here to make the construction of ConvNet easy.

    Attributes
    -------------
        conv : FullyConvolutionnal
            The convolution part

        fc : FullyConnected
            The fully connected part
    """
    def __init__(self, img_size, conv_archi, fc_archi, activation_function=nn.ReLU, **kwargs):
        """Instantiate a ConvNet object.

        Parameters
        ------------
            img_size : tuple of int
                Height, Width and number of channels of the image

            conv_archi : list of dict
                Architecture defines how will the convolutionnal part be.
                Each term of the list has to have two items :
                {"filter": nb_filter, "nb_conv": nb_convolutions}
                See utils.conv_architecture for an example

            fc_archi : list of int
                Each int of the list is the size of the corresponding layer

            activation_function : nn.Module
                Activation function between two convolutions and two fully connected blok

            **kwargs : dict
                This is given to utils.conv_architecture
        """
        super(ConvNet, self).__init__()
        self.conv = FullyConvolutionnal(conv_archi, activation_function, img_size, **kwargs)
        self.fc = FullyConnected(self.conv.flattenned_size, fc_archi, activation_function)

    def forward(self, x):
        conv_out = self.conv(x)
        conv_out = conv_out.view(x.size(0), -1)
        return self.fc(conv_out)
