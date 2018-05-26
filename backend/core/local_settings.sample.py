from .settings import *

NODE_ENV = os.getenv('NODE_ENV', default="development")

if DEBUG:
    MIDDLEWARE.append('api.middleware.dev_cors_middleware')

if not DEBUG and NODE_ENV == "production":
    STATICFILES_DIRS.append(os.path.join(REACT_APP_DIR, 'build', 'static'))
