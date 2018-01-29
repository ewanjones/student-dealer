from settings_base import *

ALLOWED_HOSTS = ['178.62.17.227']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'student-dealer',
        'USER': 'postgres',
        'PASSWORD': 'SD14dealer',        
    }
}
