#!/usr/bin/env python

from setuptools import setup


setup(
    name='libyear',
    version='0.1.0',
    description='A simple measure of software dependency freshness.',
    long_description=open('README.md').read(),
    author='nasirhjafri',
    url='https://github.com/nasirhjafri/libyear',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['libyear'],
    py_modules=['libyear'],
    scripts=['libyear/libyear'],
    dependency_links=[
    ],
    install_requires=[
        'requests==2.22.0',
        'prettytable==0.7.2',
        'python-dateutil==2.8.1',
    ],
)
