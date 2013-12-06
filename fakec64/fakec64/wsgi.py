"""
WSGI config for fakec64 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import site
import sys
site.addsitedir('/www/sites/c64.qj.no/virtualenv/fakec64/lib/python2.6/site-packages')
sys.path.insert(0, '/www/sites/c64.qj.no/fakec64/fakec64')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fakec64.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
