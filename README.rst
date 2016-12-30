pyipa: a lib for parsing IPA files
----------------------------------

This is a library to easily extract information from IPA files, and also a command line utility to do that

Usage
-----
::

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



Contribute
----------

#. Fork the project on github to start making your changes
#. Send pull requests with your bug fixes or features
#. Submit and create issues on github


TODO
----
- Cli doesn't extract Icons from a Newstand IPA
