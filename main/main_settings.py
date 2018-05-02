from django.conf import settings

proxies = None

PROXIES = getattr(settings, 'MAIN_PROXIES', proxies)
