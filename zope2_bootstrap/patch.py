from AccessControl import ClassSecurityInfo
from App.special_dtml import DTMLFile
from App.Management import Navigation
from OFS.ObjectManager import ObjectManager
import Products
import os

security = ClassSecurityInfo()
security.declarePublic('manage_zmi_logout')


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
