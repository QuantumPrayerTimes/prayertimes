#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read().strip()
VERSION = "0.1"

setup(
    name='prayertimes',
    version=VERSION,
    description='An Islamic project aimed at providing an open-source library for calculating Muslim prayers times.',
    long_description=README,
    author='Sid-Ali TEIR',
    author_email='git.syedelec@gmail.com',
    maintainer='Sid-Ali TEIR',
    maintainer_email='git.syedelec@gmail.com',
    url='https://github.com/QuantumPrayerTimes/prayertimes',
    license='LGPL v3.0',
    package_data={
        '': ['README.rst'],
    },
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=['nose'],
)
