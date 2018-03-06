#!/usr/bin/env python
"""web.py: makes web apps (http://webpy.org)"""

from __future__ import generators

__version__ = "1.0"
__author__ = [
    "dm <deathmemory@163.com>",
]
__license__ = "public domain"
__contributors__ = "see http://webpy.org/changes"

from . import dex, dex_ints, leb128


from .dex import *
from .dex_ints import *
from .leb128 import *
