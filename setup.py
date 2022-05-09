from setuptools import setup, find_packages

setup(
    name='ermin-standards',
    version='0.1.0',
    packages=find_packages(include=['ermin-standards', 'ermin.*'])
)