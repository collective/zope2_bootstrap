from setuptools import find_packages
from setuptools import setup
import os


VERSION = '0.0.8'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description="ZMI Bootstrapped",
    include_package_data=True,
    install_requires=[
        'collective.monkeypatcher',
    ],
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read()),
    name='zope2_bootstrap',
    packages=find_packages(),
    url='https://github.com/aclark4life/zope2_bootstrap',
    version=VERSION,
)
