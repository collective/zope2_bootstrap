test:
	flake8 zope2_bootstrap/*.py
	check-manifest
	pyroma .
	viewdoc
