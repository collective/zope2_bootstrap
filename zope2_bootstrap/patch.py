from AccessControl import ClassSecurityInfo
from App.special_dtml import DTMLFile
from App.Management import Navigation
from OFS.ObjectManager import ObjectManager
import Products
import os

security = ClassSecurityInfo()
security.declarePublic('manage_zmi_logout')

LOGO_HTML = """\
<div style="margin: 22px 0 22px 0">
    <a href="<dtml-var "REQUEST.SERVER_URL" html_quote>"><img
        src="<dtml-var "REQUEST.SERVER_URL"
        html_quote>/++resource++plone-logo.png"></a>
</div>
"""


ZMI_WARNING_HTML = """\
<div class="alert alert-error"><strong>Warning:</strong> <span>The Zope
Management Interface (ZMI) is a very dangerous place to be. It provides
direct access to Zope database (ZODB) objects. As such, you should not attempt
to edit, cut, copy, paste, add, or remove content or change any settings here,
unless you know exactly what you are doing. You have been warned! Changing
these settings will void any and all Plone warranties, both written and
implied. Please do not contact the Plone team about any site damages
that may occur as a result of ZMI changes.
</div></tr><tr>
"""


# XXX c.monkeypatcher requires a function or method
# so we give it one, though we don't need to patch
# this particular method at all
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

    # Add table classes to object listing
    main = os.path.join(here, 'main')  # OFS
    manage_main = os.path.join(here, 'manage_main')
    if has_editor():
        dtmlfile = manage_main
    else:
        dtmlfile = main
    ObjectManager.manage_main = DTMLFile(main, globals())

    # Re-apply Plone zmi hacks
    # Based on Products/CMFPlone/patches/addzmiplonesite.py
    if has_plone():
        code = Products.CMFPlone.patches.addzmiplonesite.ADD_PLONE_SITE_HTML
        main = ObjectManager.manage_main
        orig = main.read()
        pos = orig.find('<!-- Add object widget -->')

        # Add in our button html at the right position
        new = orig[:pos] + code + orig[pos:]

        # Modify the manage_main
        main.edited_source = new
        main._v_cooked = main.cook()

    # Add contextual logo
    # Based on Products/CMFPlone/patches/addzmiplonesite.py
    if has_plone():
        target = '<table cellpadding="0" cellspacing="0" width="100%"'
        target += ' border="0">'
        code = LOGO_HTML
        main = ObjectManager.manage_tabs
        orig = main.read()
        pos = orig.find(target)

        # Add in our logo HTML before the first table
        new = orig[:pos] + code + orig[pos:]

        # Modify the manage_tabs
        main.edited_source = new
        main._v_cooked = main.cook()

    # Add ZMI warning
    # Based on Products/CMFPlone/patches/addzmiplonesite.py
    if has_plone():
        target = '<table width="100%" cellspacing="0" cellpadding="2"'
        target += ' border="0">'
        code = ZMI_WARNING_HTML
        main = ObjectManager.manage_tabs
        orig = main.read()
        pos = orig.find(target)

        # Add in our logo HTML before the first table row
        new = orig[:pos] + code + orig[pos:]

        # Modify the manage_tabs
        main.edited_source = new
        main._v_cooked = main.cook()
