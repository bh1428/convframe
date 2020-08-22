#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""setup.py for convframe package"""
from setuptools import find_packages, setup

from convframe import __version__


def get_install_requires(requirements_file="requirements.in"):
    """get requirements from a file"""
    requirements = []
    with open(requirements_file) as fh_in:
        for line in fh_in:
            if (hash_pos := line.find("#")) > -1:
                line = line[:hash_pos]
            line = line.strip()
            if line:
                requirements.append(line)
    return requirements


with open("LICENSE") as f:
    license = f.read()

description = "Converter Framework - framework for simple text based converters"

setup(
    name="convframe",
    version=__version__,
    author="Ben Hattem",
    author_email="benghattem@gmail.com",
    url="https://github.com/bh1428/convframe",
    description=description,
    long_description=description,
    license=license,
    install_requires=get_install_requires(),
    packages=find_packages(exclude=("tests", "tests.*")),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)
