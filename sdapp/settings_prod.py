from sdapp.settings_base import *

ALLOWED_HOSTS = ['178.62.17.227']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'studentdealer',
	'HOST': 'localhost',
        'USER': 'sdadmin',
	'PASSWORD': 'SD14dealer'
    }
}

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdapp.settings_prod')
