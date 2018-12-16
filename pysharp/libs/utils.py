#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Harrison Feng <feng.harrison@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""pysharp.libs.utils module for various useful utility functions."""


# Remove duplicates from a sequence while maintaining order
def remove_duplicates(items):
    """Remove duplicates from a sequence while maintaining order.


    >>> from pysharp.libs.utils import remove_duplicates
    >>> l = ['a','b', 'a', 'e', 'f', 'b']
    >>> list(utils.remove_duplicates(l))
    ['a', 'b', 'e', 'f']

    >>> s = 'cvsfdfsdfsf'
    >>> ''.join(utils.remove_duplicates(s))
    'cvsfd'

    :param items iterable: A sequence contains duplicated item
    :return: A generator with duplicated item removed
    :rtype: generator
    """

    rslt = set()
    for item in items:
        if item not in rslt:
            yield item
            rslt.add(item)


def remove_duplicates_unhashable(items, key=None):
    """Remove duplicates with unhashable item contained from a sequence while
    maintaining order


    :param items iterable: A sequence contains duplicated item
    :return: A generator with duplicated item removed
    :rtype: generator
    """

    rslt = set()
    for item in items:
        v = item if key is None else key(item)
        if v not in rslt:
            rslt.add(v)