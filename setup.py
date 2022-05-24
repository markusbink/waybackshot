#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="waybackshot",
    version="0.1.0",
    description=(
        "A simple API to retrieve screenshots of webpages stored on the Wayback Machine."
    ),
    url="https://github.com/markusbink/wayback-shot",
    author="Markus Bink and Marcos Fernández-Pichel",
    author_email="markus.bink@student.ur.de and marcosfernandez.pichel@usc.e",
    license="GPLv3.0",
    packages=find_packages(),
    zip_safe=False,
    # python_requires="3.9.12",
    install_requires=[
        "requests==2.25.1",
        "selenium==4.1.5",
        "webdriver_manager==3.5.4",
    ],
)
