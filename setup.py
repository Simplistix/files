# Copyright (c) 2013 Simplistix Ltd
# See license.txt for license details.

import os, sys

if sys.version_info[:2] > (3, 0):
    from configparser import RawConfigParser
else:
    from ConfigParser import RawConfigParser
    
from setuptools import setup, find_packages

name = 'dir'
base_dir = os.path.dirname(__file__)

# read test requirements from tox.ini
config = RawConfigParser()
config.read(os.path.join(base_dir, 'tox.ini'))
test_requires = []
for item in config.get('testenv', 'deps').split():
    test_requires.append(item)
# Tox doesn't need itself, but we need it for testing.
test_requires.append('tox')

setup(
    name=name,
    version='1.0dev',
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="Handy utilities for working with files, directories and their permissions.",
    long_description=open(os.path.join(base_dir,'docs','description.txt')).read(),
    url='http://www.simplistix.co.uk/software/python/dir',
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        ],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=test_requires,
        docs=['sphinx',
              'zc.rst2',
              'pkginfo >= 1.0b2',
              'setuptools-git'],
        dev='setuptools-git'
        )
    )
