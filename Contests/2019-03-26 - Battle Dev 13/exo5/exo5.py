""" Answer a specific exercise of a programming contest.

This module contains all the code needed to answer a given exercise during a
programming contest. Due to its quick creation and the fact that it's probably
not following proper Python guidelines (as described in multiples PEP
documents), it shouldn't be used in production.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

import statistics
import math
import datetime
import collections
import sys

from itertools import permutations
from functools import lru_cache


__author__ = "Bizzozzéro Nicolas"
__contact__ = "nicolasbizzozzero[at]gmail.com"
__copyright__ = "Copyright 2019, Bizzozzéro Nicolas"
__date__ = "2019/03/26"
__license__ = "GPLv3"


def identity(*args):
    """ Always returns the same value that was used as its argument.

    Example:
    >>> identity(1)
    1
    >>> identity(1, 2)
    (1, 2)
    """
    if len(args) == 1:
        return args[0]
    return args


def parsin(*, l=1, vpl=1, cf=identity, s=" "):
    """ Can parse inputs usually used in competitive programming problems.
    Arguments:
    - l, as in "Lines", the number of lines to parse at once.
    - vpl, as in "Values Per Line", the number of values to parse per line.
    - cf, as in "Cast Function", the function to apply to each parsed element.
    - s, as in "Separator", the string separating multiple values in the same
      line.
    """
    if l == 1:
        if vpl == 1:
            return cf(input())
        else:
            return list(map(cf, input().split(s)))
    else:
        if vpl == 1:
            return [cf(input()) for _ in range(l)]
        else:
            return [list(map(cf, input().split(s)))
                    for _ in range(l)]


def find_curr_pos(grid):
    return grid.find("X")


def compute_score(res):
    score = 0
    for obj in res:
        if obj == "o":
            score += 1
        if obj == "*":
            score *= 2
    return score


def str_replace(string, index, new_char):
    return string[:index] + new_char + string[index + 1:]


def is_next_object_left(grid, curr_pos, object):
    grid_left = grid[:curr_pos][::-1]
    pos_object = grid_left.find(object)

    if pos_object == -1:
        return False

    if object == "o":
        opposite = "*"
    elif object == "*":
        opposite = "o"

    pos_opposite = grid_left.find(opposite)
    if pos_opposite == -1:
        return curr_pos + pos_object - 1
    elif pos_opposite < pos_object:
        return False
    return curr_pos + pos_object - 1


def is_next_object_right(grid, curr_pos, object):
    grid_right = grid[curr_pos + 1:]
    pos_object = grid_right.find(object)

    if pos_object == -1:
        return False

    if object == "o":
        opposite = "*"
    elif object == "*":
        opposite = "o"

    pos_opposite = grid_right.find(opposite)
    if pos_opposite == -1:
        return curr_pos + pos_object + 1
    elif pos_opposite < pos_object:
        return False
    return curr_pos + pos_object + 1


@lru_cache(maxsize=4096)
def is_perm_possible(grid, perm):
    possibilites = []
    curr_pos = find_curr_pos(grid)
    next_object = perm[0]
    perm = perm[1:]

    object_pos = is_next_object_left(grid, curr_pos, next_object)
    if object_pos is not False:
        possibilites.append(str_replace(str_replace(grid, curr_pos, "."), object_pos, "X"))

    object_pos = is_next_object_right(grid, curr_pos, next_object)
    if object_pos is not False:
        possibilites.append(str_replace(str_replace(grid, curr_pos, "."), object_pos, "X"))

    while perm != tuple():
        if possibilites == []:
            return False
        next_object = perm[0]
        perm = perm[1:]
        new_possibilities = []
        for possibility in possibilites:
            curr_pos = find_curr_pos(possibility)
            object_pos = is_next_object_left(possibility, curr_pos, next_object)
            if object_pos is not False:
                new_possibilities.append(str_replace(str_replace(possibility, curr_pos, "."), object_pos, "X"))

            object_pos = is_next_object_right(possibility, curr_pos, next_object)
            if object_pos is not False:
                new_possibilities.append(str_replace(str_replace(possibility, curr_pos, "."), object_pos, "X"))
        possibilites = new_possibilities
    return True


def generate_all_perms(all_objects):
    return permutations(all_objects)


def main():
    n = parsin(cf=int)
    grid = parsin()

    curr_pos = find_curr_pos(grid)
    all_objects = collections.Counter(grid)
    all_objects = (all_objects["*"] * "*") + (all_objects["o"] * "o")
    all_perms = generate_all_perms(all_objects)
    all_perms = list(filter(lambda p: is_perm_possible(grid, p), all_perms))

    best_perm = all_perms[0]
    best_score = compute_score(best_perm)
    for perm in all_perms[1:]:
        score = compute_score(perm)
        if score > best_score:
            best_perm = perm
            best_score = score

    print("".join(best_perm))


if __name__ == '__main__':
    main()
