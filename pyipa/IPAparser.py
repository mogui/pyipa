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

import zipfile
import plistlib
from .bplist import BPlistReader

class IPAparser(object):
  """docstring for IPAparser"""

  def __init__(self, path):
    self.path = path
    self.zip_obj = None

  def findFile(self, fileToFind):
    for filepath in self.zip_obj.namelist():
      fname = filepath.split('/')[-1]
      if fname == fileToFind:
        return filepath
    return None

  def findInfoPlist(self):
    for filepath in self.zip_obj.namelist():
      parts = filepath.split('/')
      if len(parts) > 2 and  parts[2] == 'Info.plist':
        return filepath
    return None

  def saveFileTo(self, zipfilepath, newfilename):
    raw = self.zip_obj.read(zipfilepath)
    f = open(newfilename, "w")
    f.write(raw)
    f.close()

  def parseInfo(self):
    self.zip_obj = zipfile.ZipFile(self.path, 'r')
    InfoPath = self.findInfoPlist()

    if not InfoPath:
      raise Exception("Info.plist not found")

    raw = self.zip_obj.read(InfoPath)

    try:
      InfoPlist = plistlib.readPlistFromString(raw)
    except:
      InfoPlist =  BPlistReader.plistWithString(raw)

    return InfoPlist