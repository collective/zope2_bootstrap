from setuptools import find_packages
from setuptools import setup


VERSION = '0.0.1'


setup(
    author='aclark4life',
    include_package_data=True,
    install_requires=[
        'collective.monkeypatcher',
    ],
    name='zope2_bootstrap',
    packages=find_packages(),
    version=VERSION,
)
