Introduction
============

Add Twitter Bootstrap styles to Zope Management Interface

Installation
============

Do this::

    $ virtualenv .
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit ``buildout.cfg`` to contain::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-zope2/master/2.13.x

Run Buildout and start Zope2::

    $ bin/buildout
    $ bin/zope2 fg

Enjoy **Bootstrap goodness**:

.. image:: https://github.com/aclark4life/zope2_bootstrap/raw/master/screenshot.png
.. image:: https://github.com/aclark4life/zope2_bootstrap/raw/master/screenshot2.png

.. _`Twitter Bootstrap`: http://twitter.github.com/bootstrap/index.html

