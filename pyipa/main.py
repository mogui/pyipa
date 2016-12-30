#!/usr/bin/env python
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


"""pyipa.

Usage:
  pyipa manifest <IPA> <IPA_URL> <ICON_URL> [<MANIFEST_FILENAME>]
  pyipa icons <IPA> [<OUTPUT_DIR>]
  pyipa [-k --keys=<comma_list>] [-o --out=<json>] [--icons] <IPA>
  pyipa --all [-o --out=<json>] <IPA>
  pyipa (-h | --help)
  pyipa --version

Options:
  -k --keys=<comma_list>  Keys to extracts in a comma separated list [default: CFBundleDisplayName,CFBundleIdentifier,CFBundleVersion]
  -o --out=<json>         Type of output can be json,text [default: json]
  --icons                 Extract icons in calling dir
  --all                   Extracts ALL Info.plist keys ignoring -k option
  -h --help               Show this screen.
  --version               Show version.
"""
from docopt import docopt
from pyipa import IPAparser
import sys
import json
import plistlib

DEFAULT_KEYS = ['CFBundleDisplayName', 'CFBundleIdentifier', 'CFBundleVersion']


def err(msg):
    print "ERROR: %s" % msg
    sys.exit(2)


def main():
    arguments = docopt(__doc__, version='1.0', options_first=True)

    ipa = IPAparser(arguments['<IPA>'])
    InfoPlist = ipa.parseInfo()

    #
    # Saving icon files
    #
    if arguments['icons']:
        # Old search
        icons = InfoPlist.get('CFBundleIconFiles', list())
        for icn in icons:
            icon_path = ipa.findFile(icn)
            print icon_path
            ipa.saveFileTo(icon_path, "%s-%s" % (arguments['IPA'].split('/')[-1].split('.')[0], icn))
    elif arguments['manifest']:
        display_name = InfoPlist.get('CFBundleDisplayName')
        bundle_id = InfoPlist.get('CFBundleIdentifier')
        bundle_version = InfoPlist.get('CFBundleShortVersionString')
        ipa_url = arguments['<IPA_URL>']
        icon_url = arguments['<ICON_URL>']
        manifest_path = 'manifest.plist' if arguments['<MANIFEST_FILENAME>'] is None else arguments['<MANIFEST_FILENAME>']

        manifest = {'items': [{'assets': [{'url': ipa_url, 'kind': 'software-package'},
                                          {'url': icon_url,'kind': 'display-image'},
                                          {'url': icon_url,'kind': 'full-size-image'}],
                               'metadata': {'kind': 'software', 'title': display_name, 'bundle-identifier': bundle_id,'bundle-version': bundle_version}}],
                    'custom': 'prova_paolo'
                    }

        plistlib.writePlist(manifest, manifest_path)
    else:
        key_filter = DEFAULT_KEYS
        if arguments['--keys']:
            key_filter = arguments['--keys']

        if arguments['--all']:
            d = InfoPlist
        else:
            d = dict((k, v) for k, v in InfoPlist.items() if k in key_filter)

        if arguments['--out'] == 'json':
            out = json.dumps(d, indent=2)
        elif arguments['--out'] == 'text':
            # todo: print list as text in a nicer way
            out = "\n".join([str(v) for k, v in d.items()])
            # todo: other formats??
        else:
            err('Wrong output format: %s' % arguments['--out'])

        if arguments['FILE']:
            f = open(arguments['FILE'], "w")
            f.write(out)
            f.close()
        else:
            print out

if __name__ == '__main__':
    main()
