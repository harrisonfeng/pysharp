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


"""Decorator classes and functions

**Functions**

.. autosummary::
    :nosignatures:

        time_the_func
        since

**Classes**

.. autosummary::
    :nosignatures:

"""


import time
import logging

from functools import wraps


LOG = logging.getLogger(__name__)


def time_the_func(f):
    """Decorator to time the function."""

    @wraps(f)
    def wrapper(*args, **kwargs):
        st = time.time()
        rf = f(*args, **kwargs)
        et = time.time()
        LOG.info("The execution duration of {0}: {1}".format(
            rf.__name__,
            et - st)
        )
        return rf
    return wrapper


def since(version):
    """A decorator that annotates a function to append the version when the
    function was added."""

    import re
    indent_p = re.compile(r'\n( +)')

    def wrapper(f):
        indents = indent_p.findall(f.__doc__)
        indent = ' ' * (min(len(ind) for ind in indents) if indents else 0)
        ver_anno = '\n\n{0}.. versionadded:: {1}'.format(indent, version)
        f.__doc__ = ''.join([f.__doc__.rstrip(), ver_anno])
        return f
    return wrapper
