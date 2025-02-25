import os
from whitenoise import WhiteNoise
from django.conf import settings

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SoloLeveling.settings")
application = get_wsgi_application()

application = WhiteNoise(application, root=settings.STATIC_ROOT)

app = application
