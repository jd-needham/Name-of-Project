try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Jordan Needham',
	'url': 'URL TO GET IT',
	'download_url': 'Where to dl it',
	'author_email': 'jdneedham@hotmail.com',
	'version': '0.1',
	'install_requires': ['nose'].
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
	}

setup(**config)
