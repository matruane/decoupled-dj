from .base import *

SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
STATIC_ROOT = env("STATIC_ROOT")

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True