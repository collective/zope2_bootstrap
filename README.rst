Introduction
============

The Zope Management Interface, `Bootstrapped`_.

Installation
------------

::

    $ virtualenv-2.7 .
    $ bin/pip install zc.buildout
    $ cat > buildout.cfg << EOF
    [buildout]
    extends = https://raw.githubusercontent.com/plock/pins/master/plone-4-3
    
    [plone]
    eggs = 
        Zope2
        zope2_bootstrap
    zcml = 
        zope2_bootstrap
    EOF
    $ bin/buildout
    $ bin/plone fg

.. image:: https://github.com/aclark4life/zope2_bootstrap/raw/master/screenshot.png
.. image:: https://github.com/aclark4life/zope2_bootstrap/raw/master/screenshot2.png

.. _`Bootstrapped`: http://getbootstrap.com/
