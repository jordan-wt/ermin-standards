from setuptools import setup, find_packages

setup(
    name='ermin-standards',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "pandas>=1.1.2, < 1.3.0",
        "validators>=0.18.0",
        "numpy>=1.22",
    ]
)