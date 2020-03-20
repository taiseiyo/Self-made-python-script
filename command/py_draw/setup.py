#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="py_draw",
    version="0.0.2",
    description="This program is drawing tool written using pygame",
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
