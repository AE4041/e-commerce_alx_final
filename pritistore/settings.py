"""
Django settings for pritistore project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", ".now.sh"]  # Add your domain here for production

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    'compressor',
    'pritistore'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]

ROOT_URLCONF = 'pritistore.urls'  # Updated project name

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
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'pritistore.wsgi.application'  # Updated project name

AUTH_USER_MODEL = 'accounts.Account'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'pritistore',
    #     'USER': 'pritistore',
    #     'PASSWORD': 'q!Xtyoj@cTt2gH',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATIC_URL = '/static/'
# #STATIC_ROOT = BASE_DIR / 'static'
# STATIC_ROOT = os.path.join(BASE_DIR, "/static")
# STATICFILES_DIRS = [
#     BASE_DIR / 'pritistore/static',  # Updated project name
# ]
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, "pritistore/static")]
# STATIC_URL = '/static/'
# #STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [BASE_DIR / 'static']  # Add this line if your static files are in 'templates'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'   # For collectstatic output
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'pritistore/static')]  # Static files in 'pritistore/static'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files configuration
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Media files directory


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# SMTP config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'awuleynovember@gmail.com'
EMAIL_HOST_PASSWORD = 'qral fech rfmg ihjp'
EMAIL_USE_TLS = True
