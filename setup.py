# -*- coding: utf-8 -*-
#
# Author: Daniel Manrique-Vallier
# Maintainer(s): Tarak Shah, Patrick Ball, Daniel Manrique-Vallier
#
# License: (c) Daniel Manrique-Vallier 2018, GPL v2 or newer

from setuptools import setup


setup(
    name='jsweave',
    version='0.1',
    description='weave values by name from json name:value into LaTeX',
    url='https://github.com/HRDAG/jsweave',
    author='Daniel Manrique-Vallier',
    license='GPL',
    packages=['jsweave'],
    zip_safe=True,
    scripts=['bin/jsweave'],
)

# done.
