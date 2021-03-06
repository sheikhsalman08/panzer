"""
Django settings for PanZer project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import mongoengine


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'snvcod0^p(^6gx8ug-!$a32y8pzaed31it5^5e*_)45@a7na=6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_mongoengine',
    # 'mongoengine.django.mongo_auth',

    'crud',
    'offer',
    'api'
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

ROOT_URLCONF = 'PanZer.urls'

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

WSGI_APPLICATION = 'PanZer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'PanZer',  
#         'USER': 'root',                      
#         'PASSWORD': '',                  
#         'HOST': '',                      
#         'PORT': '',     
#     }
# }


DBNAME = 'PanZer'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
mongoengine.connect(DBNAME,host=MONGO_HOST, port=MONGO_PORT)

# This is a dummy django model. It's just a crutch to keep django content,
# while all the real functionality is associated with MONGOENGINE_USER_DOCUMENT
# AUTH_USER_MODEL = 'mongo_auth.MongoUser'

MONGOENGINE_USER_DOCUMENT = 'users.models.User'

# Don't confuse Django's AUTHENTICATION_BACKENDS with DRF's AUTHENTICATION_CLASSES!
AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
    #'django.contrib.auth.backends.ModelBackend'
)

DEFAULT_AUTHENTICATION_CLASSES = (
    'rest_framework.authentication.SessionAuthentication',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
# LOGOUT_URL = '/enter/'



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


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         # 'rest_framework.permissions.DjangoModelPermissions',
#         # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
#          'rest_framework.permissions.AllowAny',
#     )
# }

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#         # 'rest_framework.renderers.BrowsableAPIRenderer',
#     )
# }