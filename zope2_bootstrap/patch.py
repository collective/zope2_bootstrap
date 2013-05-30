from .config import LOGOUT_HTML
from .config import PLONE_LOGO_HTML
from .config import ZOPE_LOGO_HTML
from .config import ZMI_WARN_HTML
from AccessControl import ClassSecurityInfo
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


here = os.path.dirname(__file__)


class Overview:
    """
    """


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
    RESPONSE.setBody(LOGOUT_HTML)
    return


def has_plone():
    return hasattr(Products, 'CMFPlone')


# XXX We don't actually use any of the arguments passed in here.
def apply_patch(scope, original, replacement):
    """
    Patch DTML files
    """

    # Use Twitter Bootstrap CSS/JavaScript
    manage_main = os.path.join(here, 'manage_main')  # Our custom manage_main
    manage_page_style = os.path.join(here, 'static', 'css', 'bootstrap.css')
    manage_page_script = os.path.join(here, 'static', 'js', 'bootstrap.js')
    manage_page_header = os.path.join(here, 'manage_page_header')
    manage_page_footer = os.path.join(here, 'manage_page_footer')

    dtmlfile = DTMLFile(manage_page_style, globals())
    setattr(Navigation, 'manage_page_style.css', dtmlfile)

    dtmlfile = DTMLFile(manage_page_script, globals())
    setattr(Navigation, 'manage_page_script.js', dtmlfile)

    dtmlfile = DTMLFile(manage_page_header, globals())
    setattr(Navigation, 'manage_page_header', dtmlfile)

    dtmlfile = DTMLFile(manage_page_footer, globals())
    setattr(Navigation, 'manage_page_footer', dtmlfile)

    # Use class="table" on folder contents
    ObjectManager.manage_main = DTMLFile(manage_main, globals())

    # Add ZMI warning
    target = '<table width="100%" cellspacing="0" cellpadding="2"'
    target += ' border="0">'
    code = ZMI_WARN_HTML
    main = ObjectManager.manage_tabs
    orig = main.read()
    pos = orig.find(target)
    new = orig[:pos] + code + orig[pos:]
    main.edited_source = new
    main._v_cooked = main.cook()

    # Add logo
    target = '<table cellpadding="0" cellspacing="0" width="100%"'
    target += ' border="0">'
    if has_plone():
        code = PLONE_LOGO_HTML
    else:
        code = ZOPE_LOGO_HTML
    main = ObjectManager.manage_tabs
    orig = main.read()
    pos = orig.find(target)
    new = orig[:pos] + code + orig[pos:]
    main.edited_source = new
    main._v_cooked = main.cook()
