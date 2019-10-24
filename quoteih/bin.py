#!/usr/bin/python

from __future__ import print_function
import requests
from random import randint

"""
Modified by sn3ksoftware for more portability
(only external import required is Requests).
Also, exception handling for prettier errors.
Orginial URL:
https://gist.github.com/bgalvao/f59d10229693a3a2a4cb1b7cad7a9d2b

License: NoLicense Source (Source code with no license.)
"""

def ansi(code_r, bold=""):
    """ANSI Colours for printing (Because why not?)
    Code can be 30-37. In order of colours,
    these are black, red, green, yellow,
    blue, magnenta, cyan, and white.
    After every colour print, print ansi(0) to clear colour attributes.
    (Copied from psilib.utils.ansi)
    """
    ansi_base = "\033"
    code = str(code_r)
    if bold:
        ansi_code = ansi_base + "[" + code + ";1m"
        return ansi_code
    else:
        ansi_code = ansi_base + "[" + code + "m"
        return ansi_code

# after probing, I found out that these are the possible values
# [0, 140]
url = "https://indie-hackers.firebaseio.com/loadingQuotes/{}.json".format(
        randint(0, 140)
)

# try to get url
try:
    data = requests.get(url).json()
except requests.exceptions.ConnectionError:
    print(
            ansi(31),
            "\nE: Could not retrieve quote from {}".format(url),
            "\n",
            ansi(0),
            sep=""
            )
    exit()

quote = data['quote']
founder, company = data['byline'].split('of')

print(
        ansi(32),
        '\n"{quote}"'.format(quote=quote),
        ansi(0),
        "\n- ",
        ansi(31, bold=True),
        founder,
        ansi(0),
        "of",
        ansi(36, bold=True),
        company,
        ansi(0),
        "\n",
        sep=""
        )

#print(ansi(36) + '(www.indiehackers.com)' + ansi(0) + '\n')
