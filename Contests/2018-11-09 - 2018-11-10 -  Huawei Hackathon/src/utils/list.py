import itertools


def flatten(lst):
    """ Flatten a list object until it do not have any depth.
    If the object passed as a parameter is not a list, it will be converted as
    such.
    :param lst: The list to flatten.

    Examples:
    >>> flatten([4, 8, 15, 16, 23, 42])
    [4, 8, 15, 16, 23, 42]
    >>> flatten([[4, 8, 15, 16, 23, 42]])
    [4, 8, 15, 16, 23, 42]
    >>> flatten([[[4, 8, 15, 16, 23, 42]]])
    [4, 8, 15, 16, 23, 42]
    """
    while True:
        try:
            lst = list(itertools.chain(*lst))
            if type(lst[0]) != list:
                return lst
        except TypeError:
            return list(lst)
        except IndexError:
            return lst


def removes_indexes(lst, indexes):
    """ Remove all indexes from a list.
    :param lst: The list to remove the indexes from.
    :param indexes: The indexes to remove from the list.
    :return: A copy of the list with all items removed at specific indexes.

    Examples:
    >>> removes_indexes([4, 8, 15, 16, 23, 42], [0, 2, 5])
    [8, 16, 23]
    >>> removes_indexes([4, 8, 15, 16, 23, 42], [0, 2, -1])
    [8, 16, 23]
    """
    lst = lst.copy()
    for index in sorted(indexes, reverse=True):
        del lst[index]
    return lst


if __name__ == '__main__':
    pass
