#!/bin/python3

import setuptools

setuptools.setup(
    name='lipam',
    version='1.0',
    packages=[
            'lipam'
    ],
    author='Fritz Grimpen',
    author_email='fritz@grimpen.net',
    url='https://github.com/fritz0705/lipam',
    license='https://opensource.org/licenses/MIT',
    description='Simple IP Address management system for the CLI',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: System :: Networking',
            'Topic :: System :: Systems Administration'
    ],
    install_requires=[
        'lglass',
        'netaddr'
    ],
    entry_points={
        'console_scripts': [
            'lipam = lipam.cli:main'
        ]
    },
    package_data={
    }
)
