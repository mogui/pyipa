# -*- coding: utf-8 -*-

#
# The MIT License (MIT)
# Copyright (c) 2014, Niko Usai <mogui83@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

"""
pyipa
~~~~~~~~

:copyright: (c) 2014 Niko Usai
:license: see LICENSE for more details.

"""

__title__ = 'pyipa'
__version__ = '1.0.1'
__description__ = 'Python module to extract useful info from an IPA'
__url__ = 'https://github.com/mogui'
__build__ = 0
__author__ = 'Niko Usai'
__author_email__ = 'mogui83@gmail.com'
__license__ = 'ISC'
__copyright__ = 'Copyright 2014 Niko Usai'


from .IPAparser import IPAparser
from .bplist import BPlistReader, BPListWriter