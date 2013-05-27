LOGOUT_HTML = """<html>
<head><title>Logout</title></head>
<body>
    <p>
        You have been logged out. For real.
    </p>
</body>
</html>
"""

PLONE_LOGO_HTML = """\
<div style="margin: 22px 0 22px 0">
    <a href="<dtml-var "REQUEST.SERVER_URL" html_quote>"><img
        src="<dtml-var "REQUEST.SERVER_URL"
        html_quote>/++resource++plone-logo.png"></a>
</div>
"""

ZOPE_LOGO_HTML = """\
    <a href="<dtml-var "REQUEST.SERVER_URL" html_quote>"><img
        src="<dtml-var "REQUEST.SERVER_URL"
        html_quote>/p_/zopelogo_jpg"></a>
"""

ZMI_WARNING_HTML = """\
<div class="alert alert-error"><strong>Warning:</strong> <span>The Zope
Management Interface (ZMI) can be a dangerous place. It provides
direct access to Zope database (ZODB) objects. As such, you should not attempt
to edit, cut, copy, paste, add, or remove any content or change any settings
here, unless you know exactly what you are doing. You have been warned!
</div></tr><tr>
"""
