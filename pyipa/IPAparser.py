
import zipfile
import plistlib
from .bplist import BPlistReader

class IPAparser(object):
  """docstring for IPAparser"""

  def __init__(self, path):
    self.path = path

  def parseInfo(self):

    zip_obj = zipfile.ZipFile(self.path, 'r')
    filenames = zip_obj.namelist()

    InfoPath = None

    for filepath in filenames:
      fname = filepath.split('/')[-1]
      if fname == 'Info.plist':
        InfoPath = filepath
        break

    if not InfoPath:
      raise Exception("Info.plist not found")

    raw = zip_obj.read(InfoPath)

    try:
      InfoPlist = plistlib.readPlistFromString(raw)
    except:
      InfoPlist =  BPlistReader.plistWithString(raw)

    return InfoPlist