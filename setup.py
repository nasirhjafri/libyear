#!/usr/bin/env python

from setuptools import setup


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;
    that is, it is not blank, a comment, or editable.
    """
    # Remove whitespace at the start/end of the line
    line = line.strip()

    # Skip blank lines, comments, and editable installs
    return not (
            line == '' or
            line.startswith('-r') or
            line.startswith('#') or
            line.startswith('-e') or
            line.startswith('git+')
    )


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.strip() for line in open(path).readlines()
            if is_requirement(line)
        )
    return list(requirements)


setup(
    name='libyear',
    version='0.0.1',
    description='A simple measure of software dependency freshness.',
    long_description=open('README.md').read(),
    author='nasirhjafri',
    url='https://github.com/nasirhjafri/libyear',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Development Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['libyear'],
    dependency_links=[
    ],
    install_requires=load_requirements('requirements.txt'),
)
