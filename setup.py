from setuptools import find_packages
from setuptools import setup
import os


VERSION = '0.0.8'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description="Add Twitter Bootstrap to Zope Management Interface",
    include_package_data=True,
    install_requires=[
        'collective.monkeypatcher',
    ],
    long_description=(open('README.rst').read() + '\n'
        open(os.path.join('docs', 'HISTORY.txt')).read()),
    name='zope2_bootstrap',
    packages=find_packages(),
    url='https://github.com/aclark4life/zope2_bootstrap',
    version=VERSION,
)
