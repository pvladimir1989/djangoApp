import os

CACHES_BACKEND = os.getenv('CACHES_BACKEND', False)

if CACHES_BACKEND:
    REDIS_URL = os.getenv('REDIS_URL')
    CACHES = {
        "default": {
            "BACKEND": CACHES_BACKEND,
            "LOCATION": REDIS_URL,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        },
    }
