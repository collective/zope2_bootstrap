
Introduction
============

This does what you think it does: applies `Twitter Bootstrap`_ styles to Zope2.

Installation
============

Do this::

    $ virtualenv .
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit ``buildout.cfg`` to include::

    [buildout]
    extends = http://pythonpackages.com/buildout/zope2/2.13.x-dev

    [zope2]
    eggs += zope2_bootstrap
    zcml += zope2_bootstrap

Run buildout and start Zope2::

    $ bin/buildout
    $ bin/zope2

Enjoy **Bootstrap goodness**. It's not great, but it's better.

.. _`Twitter Bootstrap`: http://twitter.github.com/bootstrap/index.html

.. image:: https://github.com/aclark4life/zope2_bootstrap/raw/master/screenshot.png

