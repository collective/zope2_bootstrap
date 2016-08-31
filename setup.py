from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.3.0'

setup(author='Alex Clark',
      author_email='aclark@aclark.net',
      classifiers=[
          'Programming Language :: Python :: 2.7',
      ],
      description="Zope Management Interface with Bootstrap",
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      keywords='Bootstrap Zope Management Interface ZMI',
      include_package_data=True,
      install_requires=[
          'collective.monkeypatcher',
      ],
      license='GPL',
      long_description=(
          open('README.rst').read() + '\n' + open('CHANGES.rst').read()),
      name='zope2_bootstrap',
      packages=find_packages(),
      test_suite='tests.TestCase',
      url='https://github.com/collective/zope2_bootstrap',
      version=VERSION,
      zip_safe=False, )
