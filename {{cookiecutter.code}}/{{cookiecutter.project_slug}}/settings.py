"""
Django settings for {{cookiecutter.project_slug}} project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

ALLOWED_HOSTS = ['{{cookiecutter.project_slug}}.juntagrico.science', 'localhost',]

ADMINS = (
    ('Admin', os.environ.get('JUNTAGRICO_ADMIN_EMAIL')),
)
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    '{{cookiecutter.project_slug}}',
    'juntagrico',
    'fontawesomefree',
    'import_export',
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
]

ROOT_URLCONF = '{{cookiecutter.project_slug}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'debug' : DEBUG,
        },
    },
]

WSGI_APPLICATION = '{{cookiecutter.project_slug}}.wsgi.application'

# HTTP

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','{{cookiecutter.project_slug}}.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'),
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'),
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False),
    }
}

# Email

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25'))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'de'
DATE_INPUT_FORMATS =['%d.%m.%Y']

TIME_ZONE = 'Europe/Zurich'
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# django.contrib.staticfiles
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# django.contrib.sites Settings

SITE_ID = 1


# django.contrib.auth Settings

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)

LOGIN_REDIRECT_URL = "/"


# django.contrib.sessions Settings

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


# impersonate Settings

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}


# crispy_form Settings

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# import_export Settings

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'


# juntagrico Settings

ORGANISATION_NAME = "{{cookiecutter.organisation_name}}"
ORGANISATION_LONG_NAME = "{{cookiecutter.organisation_name}}"
ORGANISATION_ADDRESS = {"name":"{{cookiecutter.organisation_name}}", 
            "street" : "{{cookiecutter.street}}",
            "number" : "{{cookiecutter.number}}",
            "zip" : "{{cookiecutter.zip}}",
            "city" : "{{cookiecutter.city}}",
            "extra" : "{{cookiecutter.extra}}"}
ORGANISATION_BANK_CONNECTION = {"PC" : "{{cookiecutter.PC}}",
            "IBAN" : "{{cookiecutter.IBAN}}",
            "BIC" : "{{cookiecutter.BIC}}",
            "NAME" : "{{cookiecutter.NAME}}",
            "ESR" : "{{cookiecutter.ESR}}"}
ORGANISATION_WEBSITE = {
    'name': "{{cookiecutter.server_url}}",
    'url': "https://{{cookiecutter.server_url}}"
}

CONTACTS = {
    "general": "{{cookiecutter.info_email}}"
}

ENABLE_SHARES = True
SHARE_PRICE = "{{cookiecutter.share_price}}"

STYLES = {'static': ['{{cookiecutter.project_slug}}/css/customize.css']}
