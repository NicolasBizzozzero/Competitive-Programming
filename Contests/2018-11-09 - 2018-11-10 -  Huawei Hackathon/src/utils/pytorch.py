import torch


def get_current_device():
    """ Check if cuda is available on the current system and return the cuda's
    device. If cuda is not available on your system, return a CPU's device.
    """
    return torch.cuda.current_device() if torch.cuda.is_available() else -1


if __name__ == '__main__':
    pass
