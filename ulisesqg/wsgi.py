"""
WSGI config for ulisesqg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')
load_dotenv(env_path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ulisesqg.settings")

application = get_wsgi_application()
