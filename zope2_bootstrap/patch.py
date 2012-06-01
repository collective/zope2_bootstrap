from AccessControl import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from App.special_dtml import DTMLFile
from App.Management import Navigation
import os

security = ClassSecurityInfo()
security.declarePublic('manage_zmi_logout')


# XXX Provide bogus class method to c.monkeypatcher
def manage_zmi_logout(self, REQUEST, RESPONSE):
    """Logout current user"""
    p = getattr(REQUEST, '_logout_path', None)
    if p is not None:
        return apply(self.restrictedTraverse(p))

    realm=RESPONSE.realm
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


# XXX Use callable to do the actual work
def apply_patch(scope, original, replacement):
    here = os.path.dirname(__file__)
    manage_page_style = os.path.join(here, 'bootstrap', 'css', 'bootstrap.css')
    dtmlfile = DTMLFile(manage_page_style, globals())
    security.declarePublic('manage_page_style.css')
    setattr(Navigation, 'manage_page_style.css', dtmlfile)
    InitializeClass(Navigation) 
