from pathlib import Path

from distutils.core import setup


setup(
    name='pyforms',
    version='1.0.0',
    author='ttrently',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only'
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=[
        'src/pyforms'
    ],
    install_requires=[
        'PyQt5',
        'jsonschema'
    ]
)
