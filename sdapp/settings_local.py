from sdapp.settings_base import *

DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sd.student-dealer'),
    }
}

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']
