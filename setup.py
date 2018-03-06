#!/usr/bin/env python

from setuptools import setup
from dex_parser import __version__

setup(name='dex_parser',
      version=__version__,
      description='web.py: makes web apps',
      author='dm',
      author_email='deathmemory@163.com',
      maintainer='dm',
      maintainer_email='deathmemory@163.com',
      url='http://webpy.org/',
      packages=['dex_parser'],
      install_requires=[
          'cheroot',
      ],
      long_description="Think about the ideal way to write a web app. Write the code to make it happen.",
      license="Public domain",
      platforms=["any"],
     )