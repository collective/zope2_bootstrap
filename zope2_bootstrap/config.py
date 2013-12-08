LOGO_PLONE_HTML = """\
<div style="margin: 22px 0 22px 0">
    <a href="<dtml-var "REQUEST.SERVER_URL" html_quote>"><img
        src="<dtml-var "REQUEST.SERVER_URL"
        html_quote>/++resource++plone-logo.png"></a>
</div>
"""

LOGO_ZOPE_HTML = """\
    <a href="<dtml-var "REQUEST.SERVER_URL" html_quote>"><img
        src="<dtml-var "REQUEST.SERVER_URL"
        html_quote>/++resource++VlogoWhite250.gif"></a>
"""

LOGOUT_HTML = """<html>
<head><title>Logout</title></head>
<body>
    <p>
        You have been logged out. For real.
    </p>
</body>
</html>
"""

ZMI_WARN_HTML = """
<div class="alert alert-warning alert-dismissable">
    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
    <strong>Warning:</strong> the <span>Zope Management Interface (ZMI)
    provides direct access to Zope database objects (ZODB).
    You should not attempt to edit, cut, copy, paste, add or
    remove any content, or change any settings here, unless you know exactly
    what you are doing.
</div>
"""
