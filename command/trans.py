#!/usr/local/bin/python3.7
import sys
import fileinput
import json
from googletrans import Translator
import mimetypes

path1 = "test.txt"


def savefile():
    f = open(path1, "r", encoding="utf-8")
    data = f.read()
    data = deform(str(data))
    f = open(path1, "w")
    f.write(data)


def deform(data):
    data = data.strip()
    data = data.replace("'", "")
    data = data.replace("\n", "")
    data = data.replace("True", "true")
    data = data.replace("False", "false")
    return data


def parse(data):
    arg = sys.argv
    data = data[int(arg[1]):int(arg[2])]
    return data


def show(data):
    f = open(path1, "r")
    data = str(f.read())
    data = parse(data)
    translator = Translator()
    jatext = translator.translate(data, src='en', dest='ja').text
    jatext = str(jatext)
    return jatext


def cut(jatext):
    for count, i in enumerate(jatext):
        if(i == "。"):
            print("。\n")
        else:
            print(i, end="")


def main():
    data = savefile()
    jatext = show(data)
    cut(jatext)

main()
