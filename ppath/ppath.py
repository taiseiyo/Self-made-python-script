#!/usr/bin/env python3
import os
import argparse
import sys


def pmodule(module):
    module_list = []
    count = 0
    for nfile in sys.path:
        file_name = nfile+"/"+module+".py"
        module_list.append(file_name)
    for files in module_list:
        if(os.path.isfile(files)):
            name = files
            open_file(name)
            count = count+1
    if (count == 0):
        print("may be package")


def parsers():
    parser = argparse.ArgumentParser(description="option setting")
    parser.add_argument("-m", "--module", help="moduleing my PYTOHNPATH")
    opt = parser.parse_args()
    return opt


def open_file(name):
    if(name != None):
        f = open(name, "r")
        print(f.read())
        f.close()
    else:
        pass


def main():
    opt = parsers()
    pmodule(opt.module) if \
        opt.module != None else None


main()
