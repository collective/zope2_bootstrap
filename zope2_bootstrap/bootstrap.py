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


# Based on
#    https://github.com/plone/Products.CMFPlone/blob/master/Products/\
#    CMFPlone/browser/admin.py#L34
#
class AppTraverser(DefaultPublishTraverse):
    """
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


def monkeypatch(scope, original, replacement):
    """
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
    cook(html, main, target)

    # Add logo

    target = '<table cellpadding="0" cellspacing="0" width="100%"'
    target += ' border="0">'

    if has_plone():
        html = PLONE_LOGO
    else:
        html = ZOPE_LOGO

    main = ObjectManager.manage_tabs
    cook(html, main, target)


def cook(html, main, target):
    """
    """

    orig = main.read()
    pos = orig.find(target)
    new = orig[:pos] + html + orig[pos:]
    main.edited_source = new
    main._v_cooked = main.cook()


# c.monkeypatcher requires a function or method so we give it this one, even
# though we don't need to patch it.
#
def manage_zmi_logout(self, REQUEST, RESPONSE):
    """
    """

    p = getattr(REQUEST, '_logout_path', None)
    if p is not None:
        return apply(self.restrictedTraverse(p))

    realm = RESPONSE.realm
    RESPONSE.setStatus(401)
    RESPONSE.setHeader('WWW-Authenticate', 'basic realm="%s"' % realm, 1)
    RESPONSE.setBody(LOGOUT)
    return


def has_plone():
    """
    """

    return hasattr(Products, 'CMFPlone')
