import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "message_board_ste_pot.settings")

application = get_wsgi_application()
