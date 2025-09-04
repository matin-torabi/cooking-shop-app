# NOTE this file extra setting like (date , cache , celery , redis and etc...)

import os
from datetime import timedelta

# custom user model
AUTH_USER_MODEL = 'authentication.CustomUser'

# redis information
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "cooking226023")
REDIS_HOST = "redis"
REDIS_PORT = 6379

# ===================
# Django Cache
# ===================
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1",  # redis 1 for django cache
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# =================
# data base
# =================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cooking',              # data base name
        'USER': 'cooking',              # user
        'PASSWORD': 'cooking226023',    # password
        'HOST': 'db',                   # service name in docker compose
        'PORT': '5432',                 # default posgresql port 
    }
}


# ===================
# Celery
# ===================
CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"  # redis 2 for celery task
CELERY_RESULT_BACKEND = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"

CELERY_ACCEPT_CONTENT    = ["json"]
CELERY_TASK_SERIALIZER   = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE          = "Asia/Tehran"

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
     }


SIMPLE_JWT = {
"ACCESS_TOKEN_LIFETIME": timedelta(days=2),
"REFRESH_TOKEN_LIFETIME": timedelta(days=365),
            }