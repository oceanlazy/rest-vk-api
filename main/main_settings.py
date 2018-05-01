from django.conf import settings

proxies = {'http': '18.218.172.146:8118', 'https': '18.218.172.146:8118'}

PROXIES = getattr(settings, 'MAIN_PROXIES', proxies)
