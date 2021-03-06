"""
Django settings for ProyectoADOA project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x!ivn84f#n%w&@!9@hf@mb67klyi^!kddjf1w+^=$c4reprqff'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = 'adoa.unla@gmail.com'
EMAIL_HOST_PASSWORD = 'pzyprxyl'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = (
    #django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    #3rd party
    'crispy_forms',
    'registration',
    'tinymce',
    'django_wysiwyg',
    'ckeditor',
    'ckeditor_uploader',
    #myapps
    'adoa',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'ProyectoADOA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ProyectoADOA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adoa',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")
MEDIA_ROOT = os.path.join(BASE_DIR, "media", "media_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "our_static"),
    #'/var/www/static/',
)

MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, "media", "our_media"),
)

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
}

##CRISPY FORMS
CRISPY_TEMPLATE_PACK = 'bootstrap3'

##DJANGO REGISTRATION REDUS SETTINGS
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

LOGIN_REDIRECT_URL =  '/'
LOGOUT_REDIRECT_URL ='/'

SITE_ID = 1


DJANGO_WYSIWYG_FLAVOR = "ckeditor" 

#CKEDITOR
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Format',
              '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize',
            ],
            [      'HorizontalRule',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'Cut','Copy','Paste','PasteText','PasteFromWord',
              '-', 'SpecialChar',
              '-', 'Source',
              '-', 'About',
            ],

        ],
        'width': 1140,
        'height': 300,
        'toolbarCanCollapse': False,
    },

    'simple_toolbar': {
        'toolbar': [
            [ 'Bold', 'Italic', 'Underline' ],
        ],
        'width': 840,
        'height': 300,
    },
}