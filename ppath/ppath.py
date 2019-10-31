#!/usr/bin/env python3
import os
import argparse
import sys


def psearch(module):
    module_list = []
    count = 0
    for nfile in sys.path:
        file_name = nfile+"/"+module+".py"
        module_list.append(file_name)
    for files in module_list:
        if(os.path.isfile(files)):
            print(files)
            count = count+1
    if (count == 0):
        print("may be package")


def parsers():
    parser = argparse.ArgumentParser(description="option setting")
    parser.add_argument("-s", "--search", help="searching my PYTOHNPATH")
    opt = parser.parse_args()
    return opt


def main():
    opt = parsers()
    psearch(opt.search) if \
        opt.search != None else None


main()
