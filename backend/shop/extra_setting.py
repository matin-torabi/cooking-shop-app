# NOTE this file extra setting like (date , cache , celery , redis and etc...)

import os
from datetime import timedelta

# custom user model
AUTH_USER_MODEL = 'authentication.CustomUser'

# ===================
# Redis Info
# ===================
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "cooking226023")
REDIS_HOST = "redis"
REDIS_PORT = 6379

# ===================
# Django Cache
# ===================
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# ===================
# Database (Postgres)
# ===================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cooking',              # database name
        'USER': 'cooking',              # user
        'PASSWORD': 'cooking226023',    # password
        'HOST': 'db',                   # service name in docker-compose
        'PORT': '5432',                 # default postgres port
    }
}

# ===================
# Celery
# ===================
#celery in redis 0
CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"

# recommended configs
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Tehran"

CORS_ALLOW_ALL_ORIGINS = True



REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", # NOTE this is auto AutoSchema drf spectacular
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
                }

SIMPLE_JWT = {
"ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
"REFRESH_TOKEN_LIFETIME": timedelta(days=365),
'ROTATE_REFRESH_TOKENS': True,
'BLACKLIST_AFTER_ROTATION': True,
            }



SPECTACULAR_SETTINGS = {
    'TITLE': 'سایت آشپزی ',
    'DESCRIPTION': 'پروژه سایت آشپزی',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    
}