from datetime import timedelta


REST_FRAMEWORK = {
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", # NOTE this is auto AutoSchema drf spectacular
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
                }

SIMPLE_JWT = {
"ACCESS_TOKEN_LIFETIME": timedelta(days=2),
"REFRESH_TOKEN_LIFETIME": timedelta(days=365),
            }