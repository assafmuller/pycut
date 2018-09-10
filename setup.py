#!/usr/bin/env python3

import setuptools


setuptools.setup(
    name='pycut',
    version='0.1',
    description='Like cut, but supports string delimiter',
    author='Assaf Muller',
    author_email='assaf@redhat.com',
    packages=setuptools.find_packages(),
    include_package_data=True,
)
