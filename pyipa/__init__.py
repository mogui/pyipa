# -*- coding: utf-8 -*-

# ___.                  __            __
# \_ |__   ____   _____/  |_  _______/  |_____________  ______
#  | __ \ /  _ \ /  _ \   __\/  ___/\   __\_  __ \__  \ \____ \
#  | \_\ (  <_> |  <_> )  |  \___ \  |  |  |  | \// __ \|  |_> >
#  |___  /\____/ \____/|__| /____  > |__|  |__|  (____  /   __/
#      \/                        \/                   \/|__|


"""
pyipa
~~~~~~~~

:copyright: (c) 2014 Niko Usai
:license: see LICENSE for more details.

"""

__title__ = 'pyipa'
__version__ = '1.0.0'
__description__ = 'Python module to extract useful info from an IPA'
__url__ = 'https://github.com/mogui'
__build__ = 0
__author__ = 'Niko Usai'
__license__ = 'ISC'
__copyright__ = 'Copyright 2014 Niko Usai'


from .IPAparser import IPAparser
from .bplist import BPlistReader, BPListWriter