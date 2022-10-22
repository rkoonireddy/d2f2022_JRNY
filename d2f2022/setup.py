#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Rohit Koonireddy",
    author_email='rohit.koonireddy@uzh.ch',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This contains all the submissions from group JRNY",
    entry_points={
        'console_scripts': [
            'd2f2022=d2f2022.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='d2f2022',
    name='d2f2022',
    packages=find_packages(include=['d2f2022', 'd2f2022.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rkoonireddy/d2f2022',
    version='0.1.0',
    zip_safe=False,
)
