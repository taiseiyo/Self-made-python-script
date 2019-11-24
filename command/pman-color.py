#!/usr/bin/env python3
import argparse
import subprocess
from subprocess import PIPE
from colorama import Fore, Back, Style


class Colors:

    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "end": "\033[0m",
        "bold": "\038[1m",
    }


def command(module):
    cmd1 = "pman -m " + module
    f1 = subprocess.Popen(cmd1.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = f1.communicate()
    out = str(out.decode("utf-8"))
    for line in out.splitlines():
        print(Fore.GREEN+line)


def parsers():
    parser = argparse.ArgumentParser(description="help options")
    parser.add_argument('-m', '--module',
                        help="choose python module")
    opt = parser.parse_args()
    return opt


def main():
    opt = parsers()
    command(opt.module) if \
        (opt.module) else None


main()
