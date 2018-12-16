#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from collections import deque


def tail(filename, n=0):
    """Return the last n lines of a file.

    :param filename str: The full path of file to be tailed.
    :param n int: The number of line to be tailed.
    :return: A deque contained lines tailed.
    :rtype: deque
    """

    if not os.path.exists(filename):
        raise OSError('The given file is not existing.')

    with open(filename, 'r') as fp:
        return deque(fp, n)
