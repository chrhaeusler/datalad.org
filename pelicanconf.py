#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'DataLad Team'
SITENAME = u'DataLad'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'better_tables', 'headerid' ]

THEME = 'theme/'

CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None

RELATIVE_URLS = False

HEADERID_LINK_CHAR = '&#xe805;'

#
# Configure the site
#
STATIC_PATHS = ['asciicast', 'css', 'js', 'img']
MENUITEMS = [ ('About', '/about.html', None),
              ('Get DataLad', '/get_datalad.html', None),
              ('Features', '/features.html', None),
              ('Datasets', '/datasets.html', None),
              ('Development', '/development.html', None),
              ('Docs', 'http://docs.datalad.org', '_blank'),
]
