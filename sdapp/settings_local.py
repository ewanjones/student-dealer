from sdapp.settings_base import *

DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'studentdealer',
    }
}

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '4e3dcf8d.ngrok.io']
