from setuptools import find_packages
from setuptools import setup

VERSION = '0.0.1'

setup(
    author='aclark4life',
    description="This does what you think it does: applies Twitter Bootstrap styles to Zope2.",
# XXX Any way to make this work with Zope2?
#    entry_points = {
#        'z3c.autoinclude.plugin': 'target = ???',
#    },
    include_package_data=True,
    install_requires=[
        'Zope2',
        'collective.monkeypatcher',
    ],
    long_description=open('README.rst').read(),
    name='zope2_bootstrap',
    packages=find_packages(),
    version=VERSION,
)
