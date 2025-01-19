"""
WSGI config for chat_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add the path to your project directory (replace with the correct path)
path = '/home/Hemanshi/Enfund_Task/enfund/chat_project'
if path not in sys.path:
    sys.path.append(path)

# Set the settings module for your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

# Get the WSGI application for your project
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
