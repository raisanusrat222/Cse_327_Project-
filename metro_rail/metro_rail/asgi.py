"""
<<<<<<< HEAD
ASGI config for MetroRail project.
=======
ASGI config for metro_rail project.


It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/

"""

import os

from django.core.asgi import get_asgi_application
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MetroRail.settings')
# <<<<<<< HEAD
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MetroRail.settings')
# =======
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metro_rail.settings')
# >>>>>>> main

application = get_asgi_application()
