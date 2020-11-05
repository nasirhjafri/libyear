#!/usr/bin/env python
from os import path

from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="libyear",
    version="0.2.1",
    description="A simple measure of software dependency freshness.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="nasirhjafri",
    url="https://github.com/nasirhjafri/libyear",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    packages=["libyear"],
    py_modules=["libyear"],
    scripts=["libyear/libyear"],
    dependency_links=[],
    install_requires=[
        "requests>=2.0.0",
        "prettytable>=0.7.2",
        "python-dateutil>=2.7.0",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
