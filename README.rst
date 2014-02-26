Introduction
============

The Zope2 Management Interface, `Bootstrapped`_.

Installation
============

Use with Zope2 e.g.::

    $ virtualenv-2.7 .
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit your ``buildout.cfg`` file to contain::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3
    
    [plone]
    eggs = 
        Zope2
        zope2_bootstrap

Or Plone e.g.::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

.. image:: https://github.com/aclark4life/zope2_bootstrap/raw/master/screenshot.png

.. _`Bootstrapped`: http://getbootstrap.com/
