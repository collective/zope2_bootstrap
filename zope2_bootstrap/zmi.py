from .config import LOGOUT
from .config import PLONE_LOGO
from .config import WARNING
from .config import ZOPE_LOGO

from App.Management import Navigation
from App.special_dtml import DTMLFile
from OFS.ObjectManager import ObjectManager
from OFS.interfaces import IApplication
from ZPublisher.BaseRequest import DefaultPublishTraverse

from zope.component import adapts
from zope.component import queryMultiAdapter
from zope.interface import Interface
from zope.publisher.interfaces import IRequest

import Products
import os


class AppTraverser(DefaultPublishTraverse):
    """
    Based on
    https://github.com/plone/Products.CMFPlone/blob/master/\
    Products/CMFPlone/browser/admin.py#L34
    """

    adapts(IApplication, IRequest)

    def publishTraverse(self, request, name):
        """
        """
        if name == 'index_html':
            view = queryMultiAdapter(
                (self.context, request), Interface, 'zope2-overview')
            if view is not None:
                return view
        return DefaultPublishTraverse.publishTraverse(self, request, name)


def apply_patch(scope, original, replacement):
    """
    Scope is the class/module that was specified. original is the string name
    of the function to replace, and replacement is the replacement function.

    Ignore scope, original and replacement and do other patching.
    """

    # Add Bootstrap

    manage_main = os.path.join('templates', 'manage_main')
    manage_page_header = os.path.join('templates', 'manage_page_header')
    manage_page_footer = os.path.join('templates', 'manage_page_footer')

    dtmlfile = DTMLFile(manage_page_header, globals())
    setattr(Navigation, 'manage_page_header', dtmlfile)

    dtmlfile = DTMLFile(manage_page_footer, globals())
    setattr(Navigation, 'manage_page_footer', dtmlfile)

    # Add table class

    ObjectManager.manage_main = DTMLFile(manage_main, globals())

    # Add warning

    target = '<table width="100%" cellspacing="0" cellpadding="2"'
    target += ' border="0">'
    html = WARNING
    main = ObjectManager.manage_tabs
    add_html(html, main, target)

    # Add logo

    target = '<table cellpadding="0" cellspacing="0" width="100%"'
    target += ' border="0">'

    if hasattr(Products, 'CMFPlone'):
        html = PLONE_LOGO
    else:
        html = ZOPE_LOGO

    main = ObjectManager.manage_tabs
    add_html(html, main, target)


def add_html(html, main, target):
    """
    Add HTML to template and set cooked attribute
    """

    orig = main.read()
    pos = orig.find(target)
    new = orig[:pos] + html + orig[pos:]
    main.edited_source = new
    main._v_cooked = main.cook()


def manage_zmi_logout(self, REQUEST, RESPONSE):
    """
    c.monkeypatcher requires a function or method so we give it this one even
    though we're not patching it.
    """

    p = getattr(REQUEST, '_logout_path', None)
    if p is not None:
        return apply(self.restrictedTraverse(p))

    realm = RESPONSE.realm
    RESPONSE.setStatus(401)
    RESPONSE.setHeader('WWW-Authenticate', 'basic realm="%s"' % realm, 1)
    RESPONSE.setBody(LOGOUT)
    return
