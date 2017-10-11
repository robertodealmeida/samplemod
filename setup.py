# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python modules',
    long_description=readme,
    author='Beto De Almeida',
    author_email='beto@dealmeida.net',
    url='https://github.com/robertodealmeida/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
