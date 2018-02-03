from sdapp.settings_base import *

ALLOWED_HOSTS = ['127.0.0.1', '178.62.17.227', 'studentdealer.co.uk', 'localhost']

DEBUG = False
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

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdapp.settings_prod')
