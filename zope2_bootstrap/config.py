LOGOUT = """
<html>
    <head>
        <title>Logout</title>
    </head>
    <body>
        <p>You have been logged out.</p>
    </body>
</html>
"""

PLONE_LOGO = """
<div style="margin: 22px 0 22px 0">
    <a href="<dtml-var "REQUEST.SERVER_URL" html_quote>"><img src="<dtml-var
        "REQUEST.SERVER_URL" html_quote>/++resource++plone-logo.png"></a>
</div>
"""

WARNING = """
<div class="alert alert-warning alert-dismissable">
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    <strong>Warning:</strong> this management interface provides direct access
    to database objects. Please do not cut, copy, paste, add, edit or delete
    content or modify settings unless you know what you're doing.
</div>
"""

ZOPE_LOGO = """
    <a href="<dtml-var "REQUEST.SERVER_URL" html_quote>"><img src="<dtml-var
        "REQUEST.SERVER_URL" html_quote>/++resource++VlogoWhite250.gif"></a>
"""
