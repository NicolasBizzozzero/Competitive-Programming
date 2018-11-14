import random

import torch
import numpy as np


def set_manual_seed(seed):
    """ Set a manual seed to the following packages :
    * Python's default random library
    * numpy
    * pytorch
    * cuda (if available)
    * scikit-learn (use the same seed as numpy)

    This function attempts to make all results produced by these librairies as
    deterministic as possible.

    :param seed: The manual seed to set.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


if __name__ == '__main__':
    pass
