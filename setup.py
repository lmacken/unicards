#!/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

setup(
    name='unicards',
    version='0.3',
    description="Convert strings into unicode playing cards",
    author='Luke Macken',
    author_email='lmacken@redhat.com',
    url='http://github.com/lmacken/unicards',
    license='GPLv3+',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Topic :: Games/Entertainment",
    ],
    keywords='python unicode cards poker deck',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
)
