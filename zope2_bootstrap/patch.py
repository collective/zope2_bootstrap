from AccessControl import ClassSecurityInfo
security = ClassSecurityInfo()


security.declarePublic('manage_zmi_logout')
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
You have been logged out.
</p>
</body>
</html>""")
    return
