#!/usr/bin/python
"""
     //   ) )  //   / /
    //___/ /  //___
   / __  (   / ___
  //    ) ) //
 //____/ / //
 -------------------
Brain, the Python Brainfuck Interpreter

Copyright (c) 2011 Sebastian Kaspari
Code modified and extended by sn3ksoftware.

All code (including changes by sn3ksoftware)
is under the WTFPL:

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
Version 2, December 2004
 
Copyright (C) 2004 Sam Hocevar
<sam@hocevar.net>

Everyone is permitted to copy and distribute
verbatim or modified copies of this license
document, and changing it is allowed as long
as the name is changed.
 
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING,
DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.

"""

from __future__ import print_function

import argparse
import sys

progname = sys.argv[0].split("/")[-1]
__version__ = "1.0.0"
__author__ = "Sebastian Kaspari/sn3ksoftware"
__copyright__ = "Copyright (c) Sebastian Kaspari, WTFPLv2."


def f(fstr):
    """f-strings for older versions of Python
    i.e 2.7 to 3.5.
    Uses globals(), which is somewhat hacky.
    """
    if type(fstr) is str:
        return fstr.format(**globals())
    else:
        return None


nocmdtxt = f("""
{progname}, the python brainfuck interpreter
v{__version__}
Run [{progname} -h] for help.
""")

# --------------- #
# --GETCH_START-- #
# --------------- #

# From http://code.activestate.com/recipes/134892/
# getch()-like unbuffered character reading
# from stdin on both Windows and Unix (Python recipe)


class _Getch:
    """Gets a single character from standard input. Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

# ------------- #
# --GETCH_END-- #
# ------------- #


def execute(filename):
    """Run brainfuck code from a file."""
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("The file does not exist!")
    else:
        evaluate(f.read())
        f.close()


def evaluate(code):
    """Evaluate brainfuck code (as a string)."""
    code = cleanup(list(code))
    bracemap = buildbracemap(code)

    cells, codeptr, cellptr = [0], 0, 0

    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
            if cellptr == len(cells):
                cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == "[" and cells[cellptr] == 0:
            codeptr = bracemap[codeptr]
        if command == "]" and cells[cellptr] != 0:
            codeptr = bracemap[codeptr]
        if command == ".":
            sys.stdout.write(chr(cells[cellptr]))
        if command == ",":
            cells[cellptr] = ord(getch.getch())

        codeptr += 1


def cleanup(code):
    """Remove anything that is not a
    brainfuck command from a string."""
    return ''.join(
        filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
    """Map open braces in brainfuck code to
    the closing braces."""
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[":
            temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap


def _main():
    """Please do NOT run this directly. It is
    only meant to be used in a script."""
    parser = argparse.ArgumentParser(
        description="Brainfuck interpreter, written in Python."
    )
    parser.add_argument(
        "-f",
        "--file",
        action="store",
        dest="filename",
        help="Run brainfuck code in file"
    )
    parser.add_argument(
        "-e",
        "--exec",
        action="store",
        dest="code",
        help="Execute brainfuck code in place"
    )
    parser.add_argument(
        "-i",
        "--interpret",
        action="store_true",
        dest="repl",
        help="Enter a basic REPL"
    )
    parser.add_argument(
        "-c",
        "--credits",
        action="store_true",
        dest="cred",
        help="show credits"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        dest="ver",
        help="show version"
    )
    result = parser.parse_args()
    
    if result.filename is not None:
        execute(result.filename)
        print("")
    elif result.code is not None:
        evaluate(result.code)
        print("")
    elif result.repl:
        try:
            while True:
                try:
                    print("\nbrain> ", end="")
                    code = input()
                except EOFError:
                    continue
                evaluate(code)
        except KeyboardInterrupt:
            print("")
            sys.exit(0)
    elif result.cred:
        print(__doc__)
    elif result.ver:
        print(f("v{__version__}"))
    else:
        print(nocmdtxt)


if __name__ == "__main__":
    try:
        _main()
    except KeyboardInterrupt:
        sys.exit(0)
