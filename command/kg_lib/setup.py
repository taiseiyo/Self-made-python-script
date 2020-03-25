#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="kg_lib",
    version="0.0.3",
    description="search book in kwansei gakuin library",
    author="suzuki taisei",
    author_email="taiseiyo11@gmail.com",
    url="https://github.com/taiseiyo/Self-made-python-script/tree/master/command/kg_lib/",
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
