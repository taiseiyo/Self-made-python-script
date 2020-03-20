#!/usr/bin/env python3
import os
from setuptools import setup, find_packages


def read_file(filename):
    path = os.path.dirname(__file__)
    filepath = os.path.join(path, filename)
    if(os.path.exists(filepath)):
        return open(filepath).read()
    else:
        return ""


setup(
    name="py_draw",
    version="0.0.4",
    description="This program is drawing tool written using pygame",
    long_description=read_file("sample.rst"),
    author="suzuki taisei",
    author_email="taiseiyo11@gmail.com",
    url="https://github.com/taiseiyo/Self-made-python-script/blob/master/command/py_draw/",
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        "pygame",
        "pyautogui",
    ],

    entry_points="""
    [console_scripts]
    py_draw = py_draw:main
"""
)
