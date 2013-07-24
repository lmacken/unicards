#!/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

setup(
    name='unicards',
    version='0.6',
    description="Convert strings into unicode playing cards",
    author='Luke Macken',
    author_email='lmacken@redhat.com',
    url='http://github.com/lmacken/unicards',
    license='ASL 2.0',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords='python unicode cards poker deck',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
)
