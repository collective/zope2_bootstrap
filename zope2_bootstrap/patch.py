from .config import LOGO_PLONE
from .config import LOGO_ZOPE
from .config import LOGOUT
from .config import ZMI_WARNING
from App.special_dtml import DTMLFile
from App.Management import Navigation
from OFS.ObjectManager import ObjectManager
from OFS.interfaces import IApplication
from ZPublisher.BaseRequest import DefaultPublishTraverse
from zope.component import adapts
from zope.component import queryMultiAdapter
from zope.interface import Interface
from zope.publisher.interfaces import IRequest
import Products
import os


# Based on https://github.com/plone/Products.CMFPlone/blob/master/Products/\
# CMFPlone/browser/admin.py#L34
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


def cook(code, main, target):
    """
    Cook resources
    """
    orig = main.read()
    pos = orig.find(target)
    new = orig[:pos] + code + orig[pos:]
    main.edited_source = new
    main._v_cooked = main.cook()


# XXX c.monkeypatcher requires a function or method so we give it one, though
# we don't need to patch this particular method at all.
def manage_zmi_logout(self, REQUEST, RESPONSE):
    """Logout current user"""
    p = getattr(REQUEST, '_logout_path', None)
    if p is not None:
        return apply(self.restrictedTraverse(p))

    realm = RESPONSE.realm
    RESPONSE.setStatus(401)
    RESPONSE.setHeader('WWW-Authenticate', 'basic realm="%s"' % realm, 1)
    RESPONSE.setBody(LOGOUT)
    return


def has_plone():
    return hasattr(Products, 'CMFPlone')


def apply_patch(scope, original, replacement):
    """
    Patch DTML
    """
    here = os.path.dirname(__file__)

    # Use Twitter Bootstrap CSS/JavaScript
    manage_main = os.path.join(here, 'manage_main')  # Our custom manage_main
    manage_page_header = os.path.join(here, 'manage_page_header')
    manage_page_footer = os.path.join(here, 'manage_page_footer')
    dtmlfile = DTMLFile(manage_page_header, globals())
    setattr(Navigation, 'manage_page_header', dtmlfile)
    dtmlfile = DTMLFile(manage_page_footer, globals())
    setattr(Navigation, 'manage_page_footer', dtmlfile)

    # Use class="table" on folder contents
    ObjectManager.manage_main = DTMLFile(manage_main, globals())

    # Add ZMI warning
    target = '<table width="100%" cellspacing="0" cellpadding="2"'
    target += ' border="0">'
    code = ZMI_WARNING
    main = ObjectManager.manage_tabs
    cook(code, main, target)

    # Add Zope or Plone logo
    target = '<table cellpadding="0" cellspacing="0" width="100%"'
    target += ' border="0">'
    if has_plone():
        code = LOGO_PLONE
    else:
        code = LOGO_ZOPE
    main = ObjectManager.manage_tabs
    cook(code, main, target)
