from .base import *

# Define development settings
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = get_secret('DATABASES')
# BROKER_URL = get_secret('REDIS_HOST')
# BROKER_VHOST = '0'

# CELERY_RESULT_BACKEND = get_secret('REDIS_HOST')
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_REDIS_DB = 0

# INSTALLED_APPS = INSTALLED_APPS + ['elasticapm.contrib.django', ]
# MIDDLEWARE = MIDDLEWARE + ['elasticapm.contrib.django.middleware.TracingMiddleware', ]
#
# CACHES = get_secret('CACHES')

# FOUNT_USER_URL = get_secret('')
# FOUNT_LOGIN_URL = get_secret('')
# FOUNT_PROFILE_URL = get_secret('')
# FOUNT_PASSWORD_RESET_URL = get_secret('')
# MEDIA_URL_PREFIX = get_secret('')
