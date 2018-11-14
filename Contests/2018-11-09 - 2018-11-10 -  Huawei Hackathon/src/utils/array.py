import numpy as np
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, Normalizer


def normalize(array, norm="l2"):
    """ Normalize samples individually to unit norm.
    Each sample (i.e. each row of the data matrix) with at least one non zero
    component is rescaled independently of other samples so that its norm (l1
    or l2) equals one.
    :param array: The array to normalize. Also works for scipy.sparse matrix
    and pandas.DataFrame with numeric values.
    :param norm: The norm to use to normalize each non zero sample. Can be
    `l1`, `l2`, or `max`
    """
    scaler = Normalizer(copy=True, norm=norm)
    return scaler.fit_transform(array)


def normalize_range(array, floor=0, ceil=1):
    """ Normalise an array between a given range.
    :param array: The array to normalize. Also works for pandas.DataFrame with
    numeric values.
    :param floor: The minimal value of the normalized range.
    :param ceil: The maximal value of the normalized range.
    """
    scaler = MinMaxScaler(feature_range=(floor, ceil), copy=True)
    return scaler.fit_transform(array)


def normalize_max_absolute(array):
    """ Normalise an array by its maximum absolute value.
    Scales and translates each feature individually such that the maximal
    absolute value of each feature in the array will be 1.0. It does not
    shift/center the data, and thus does not destroy any sparsity.
    :param array: The array to normalize. Also works for pandas.DataFrame with
    numeric values.
    """
    scaler = MaxAbsScaler(copy=True)
    return scaler.fit_transform(array)


def get_diagonal_mask(data):
    """ Return a diagonal mask computed from an array.
    Useful when the data is the same if you transpose the array, eg in a
    heatmap.

    :param data: The np.ndarray from which you want to compute the mask.
    """
    mask = np.zeros_like(data, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    return mask


def minibatches(inputs=None, targets=None, batch_size=None,
                allow_dynamic_batch_size=False, shuffle=True):
    """Generate a generator that input a group of example in numpy.array and
    their labels, return the examples and labels by the given batch size.

    Parameters
    ----------
    inputs : numpy.array
        The input features, every row is a example.
    targets : numpy.array
        The labels of inputs, every row is a example.
    batch_size : int
        The batch size.
    allow_dynamic_batch_size: boolean
        Allow the use of the last data batch in case the number of examples is
        not a multiple of batch_size, this may result in unexpected behaviour
        if other functions expect a fixed-sized batch-size.
    shuffle : boolean
        Indicating whether to use a shuffling queue, shuffle the dataset before
        return.

    Examples
    --------
    >>> X = np.asarray([['a','a'], ['b','b'], ['c','c'], ['d','d'], ['e','e'],
                        ['f','f']])
    >>> y = np.asarray([0,1,2,3,4,5])
    >>> for batch in tl.iterate.minibatches(inputs=X, targets=y, batch_size=2,
                                            shuffle=False):
    >>>     print(batch)
    (array([['a', 'a'], ['b', 'b']], dtype='<U1'), array([0, 1]))
    (array([['c', 'c'], ['d', 'd']], dtype='<U1'), array([2, 3]))
    (array([['e', 'e'], ['f', 'f']], dtype='<U1'), array([4, 5]))

    Notes
    -----
    If you have two inputs and one label and want to shuffle them together,
    e.g. X1 (1000, 100), X2 (1000, 80) and Y (1000, 1), you can stack them
    together (`np.hstack((X1, X2))`) into (1000, 180) and feed to ``inputs``.
    After getting a batch, you can split it back into X1 and X2.

    Source
    ------
    https://github.com/tensorlayer/tensorlayer/blob/6fea9d9d165da88e3354f723c89a0a6ccf7d8e53/tensorlayer/iterate.py#L15
    """
    if len(inputs) != len(targets):
        raise AssertionError(
            "The length of inputs and targets should be equal")

    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)

    # for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
    # chulei: handling the case where the number of samples is not a multiple
    # of batch_size, avoiding wasting samples
    for start_idx in range(0, len(inputs), batch_size):
        end_idx = start_idx + batch_size
        if end_idx > len(inputs):
            if allow_dynamic_batch_size:
                end_idx = len(inputs)
            else:
                break
        if shuffle:
            excerpt = indices[start_idx:end_idx]
        else:
            excerpt = slice(start_idx, end_idx)
        if (isinstance(inputs, list) or isinstance(targets, list)) and shuffle:
            # zsdonghao: for list indexing when shuffle==True
            yield [inputs[i] for i in excerpt], [targets[i] for i in excerpt]
        else:
            yield inputs[excerpt], targets[excerpt]


if __name__ == '__main__':
    pass
