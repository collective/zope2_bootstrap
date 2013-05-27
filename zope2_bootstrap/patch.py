from AccessControl import ClassSecurityInfo
from App.special_dtml import DTMLFile
from App.Management import Navigation
from OFS.ObjectManager import ObjectManager
from config import PLONE_LOGO_HTML
from config import ZOPE_LOGO_HTML
from config import ZMI_WARN_HTML
import Products
import os


security = ClassSecurityInfo()
security.declarePublic('manage_zmi_logout')


# XXX c.monkeypatcher requires a function or method so we give it one, though
# we don't need to patch this particular method at all
def manage_zmi_logout(self, REQUEST, RESPONSE):
    """Logout current user"""
    p = getattr(REQUEST, '_logout_path', None)
    if p is not None:
        return apply(self.restrictedTraverse(p))

    realm = RESPONSE.realm
    RESPONSE.setStatus(401)
    RESPONSE.setHeader('WWW-Authenticate', 'basic realm="%s"' % realm, 1)
    RESPONSE.setBody("""<html>
<head><title>Logout</title></head>
<body>
<p>
You have been logged out. For real.
</p>
</body>
</html>""")
    return


def has_editor():
    return hasattr(Products, 'ExternalEditor')


def has_plone():
    return hasattr(Products, 'CMFPlone')


# XXX Ignore params and do other work
def apply_patch(scope, original, replacement):

    # Use bootstrap css
    here = os.path.dirname(__file__)
    manage_page_style = os.path.join(here, 'bootstrap', 'css', 'bootstrap.css')
    dtmlfile = DTMLFile(manage_page_style, globals())
    security.declarePublic('manage_page_style.css')
    setattr(Navigation, 'manage_page_style.css', dtmlfile)

    # Use bootstrap js
    manage_page_script = os.path.join(here, 'bootstrap', 'js', 'bootstrap.js')
    dtmlfile = DTMLFile(manage_page_script, globals())
    security.declarePublic('manage_page_script.js')
    setattr(Navigation, 'manage_page_script.js', dtmlfile)

    manage_page_footer = os.path.join(here, 'manage_page_footer')
    ObjectManager.manage_page_footer = DTMLFile(manage_page_footer, globals())

    # Add table classes to object listing
    main = os.path.join(here, 'main')  # OFS
    manage_main = os.path.join(here, 'manage_main')
    if has_editor():
        dtmlin = manage_main
    else:
        dtmlin = main
    ObjectManager.manage_main = DTMLFile(dtmlin, globals())

    # (Re)apply Plone zmi hacks

    # Based on Products/CMFPlone/patches/addzmiplonesite.py
    if has_plone():
        code = Products.CMFPlone.patches.addzmiplonesite.ADD_PLONE_SITE_HTML
    else:
        code = ''

    main = ObjectManager.manage_main
    orig = main.read()
    pos = orig.find('<!-- Add object widget -->')

    # Add in our button html at the right position
    new = orig[:pos] + code + orig[pos:]

    # Modify the manage_main
    main.edited_source = new
    main._v_cooked = main.cook()

    # Add ZMI warning
    # Based on Products/CMFPlone/patches/addzmiplonesite.py
    target = '<table width="100%" cellspacing="0" cellpadding="2"'
    target += ' border="0">'
    code = ZMI_WARN_HTML
    main = ObjectManager.manage_tabs
    orig = main.read()
    pos = orig.find(target)

    # Add in our logo HTML before the first table row
    new = orig[:pos] + code + orig[pos:]

    # Modify the manage_tabs
    main.edited_source = new
    main._v_cooked = main.cook()

    # Add contextual logo
    # Based on Products/CMFPlone/patches/addzmiplonesite.py
    target = '<table cellpadding="0" cellspacing="0" width="100%"'
    target += ' border="0">'
    if has_plone():
        code = PLONE_LOGO_HTML
    else:
        code = ZOPE_LOGO_HTML
    main = ObjectManager.manage_tabs
    orig = main.read()
    pos = orig.find(target)

    # Add in our logo HTML before the first table
    new = orig[:pos] + code + orig[pos:]

    # Modify the manage_tabs
    main.edited_source = new
    main._v_cooked = main.cook()
