"""
WSGI config for Patent_Database project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append("Patent_Database\Patent_Database")
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'Patent_Database.settings'
application = get_wsgi_application()
