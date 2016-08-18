"""
WSGI config for ispark project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""


import os, sys, site

site.addsitedir('/home/enlighthost/webapps/ispark/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ispark.settings")

activate_this = os.path.expanduser("~/home/enlighthost/webapps/ispark/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
project = '/home/enlighthost/webapps/ispark/'
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path = ['/home/enlighthost/webapps/ispark/ispark', '/home/enlighthost/webapps/ispark'] + sys.path

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
