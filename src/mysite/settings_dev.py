import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['VEMBEDDABLE_DB_NAME'],
        'USER': os.environ['VEMBEDDABLE_DB_USER'],
        'PASSWORD': os.environ['VEMBEDDABLE_DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
