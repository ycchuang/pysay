#!/usr/bin/env python

# This file is part of pysay v1.5.1 (GitHub edition)

from distutils.core import setup

setup(name='pysay',
      version='1.5.1',
      description='A Python version of cowsay',
      author='Nicola Lamacchia',
      author_email='nicola.lamacchia@gmail.com',
      scripts=['scripts/pysay', 'scripts/pythink'],
      url='https://github.com/nicolalamacchia/pysay/',
      data_files=[('share/cows', ['cows/python.cow'])],
      license='Artistic License 2.0')
