#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="kg_lib",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        "selenium",
        "plumbum",
    ],

    entry_points="""
    [console_scripts]
    kg_lib = kg_lib:main
"""
)
