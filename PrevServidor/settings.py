"""
Django settings for PrevServidor project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from datasource.getResources import getDatabase, getEmailServer, getLoggingPsd
from prevEnums import TipoConexao

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p9@h25p2(2t37g(44li8119(@kh2eg_l(-2lrw&dbic(snk&j_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'ec2-100-24-19-48.compute-1.amazonaws.com',
    '52.91.1.60',
    'localhost',
    'newprev.dev.br',
    'newprev.dev.br:8000',
    'www.newprev.dev.br',
    'www.newprev.dev.br:8000',
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.advogado',
    'apps.escritorios',
    'apps.ferramentas',
    'apps.informacoes',
    'apps.sincron',
    'apps.newMails',
    'rest_framework',
    'django_filters',
    'drf_yasg'
]

REST_FRAMEWORK = {
    "DATE_INPUT_FORMATS": ["%Y-%m-%d"],
    "DATETIME_FORMAT": "%Y-%m-%d",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PrevServidor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PrevServidor.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = getDatabase(TipoConexao.hearthstone)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'PrevServidor/static')
                    ]

# PROJECT_ROOT = os.path.dirname(__file__)
# os.path.join(PROJECT_ROOT, '../apps')

AUTH_USER_MODEL = 'escritorios.Escritorio'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'error',
    messages.SUCCESS: 'success',
    messages.INFO: 'info',
}

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Email
emailConfig: dict = getEmailServer()

EMAIL_HOST = emailConfig['emailHost']
EMAIL_PORT = emailConfig['port']
EMAIL_HOST_USER = emailConfig['emailHostUser']
EMAIL_HOST_PASSWORD = emailConfig['emailHostPassword']
SERVER_EMAIL = emailConfig['serverEmail']
EMAIL_USE_TLS = emailConfig['emailUseTls']
EMAIL_USE_SSL = emailConfig['emailUseSsl']

# LOGS
from logging import INFO
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

sentryLogging = LoggingIntegration(
    level=INFO,
    event_level=INFO
)

sentry_sdk.init(
    dsn=getLoggingPsd(),
    integrations=[sentryLogging, DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

from logs.newLoggin import NewLogging
logs = NewLogging()