#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Max Arnold <arnold.maxim@gmail.com>'
__version__ = '0.1'

setup(
    name='fetch-google-reader',
    version=__version__,

    # Metadata for PyPI.
    author='Max Arnold',
    author_email='arnold.maxim@gmail.com',
    license='MIT',
    url='http://github.com/max-arnold/fetch-google-reader',
    keywords='google reader rss backup fetch fulltext',
    description='Google Reader RSS archive fetcher',
    long_description=open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.md')), 'rb').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ],
    scripts = ['fetch-greader.py'],
    platforms='any',
)
