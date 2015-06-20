from __future__ import unicode_literals, absolute_import
import os.path

from django.core.exceptions import ImproperlyConfigured


gettext_noop = lambda s: s


def get_env_variable(var_name, default=None):
    """Get the environment variable or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        error_msg = "Set %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

HOST_BASE_URL = None

SECRET_KEY = get_env_variable('SECRET_KEY', '')

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '..')

# Application definition
INSTALLED_APPS = (
    'alloallo.alloallo',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'alloallo', 'alloallo', 'templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ROOT_URLCONF = 'alloallo.alloallo.urls'

WSGI_APPLICATION = 'alloallo.alloallo.wsgi.application'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

LANGUAGES = (
    ('en', gettext_noop('English')),
)

LANGUAGE_CODE = 'en'

LOGIN_REDIRECT_URL = 'leagues:my'

import dj_database_url
DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ATOMIC_REQUESTS'] = True

DEFAULT_FROM_EMAIL = 'support@alloallo.eu'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = str(get_env_variable('EMAIL_HOST', ''))

# Default values, if EMAIL_HOST stay empty they will overriden
LOG_REQUESTS = True
LOG_REQUEST_ID_HEADER = "HTTP_HEROKU_REQUEST_ID"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s(%(asctime)s %(name)s %(message)s'
        },
        'sql': {
            'format': '%(asctime)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'level': 'WARN',
            'handlers': ['console'],
            'propagate': False,
        },
        'alloallo': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'alloallo.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

TWILIO_TEST_SID = 'AC2728c00f4891d511c061192e87fcb371'
TWILIO_TEST_TOKEN = '663b4ef990a9&c485#5CxQb1f9a'