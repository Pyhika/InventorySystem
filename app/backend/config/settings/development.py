import os
from .base import *

DATABASE_USER = os.getenv('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'host.docker.internal')

DATABASES = {
    'default': {
        'ENGINE':          'django.db.backends.mysql',
        'NAME':            'app',
        'USER':            DATABASE_USER,
        'PASSWORD':        DATABASE_PASSWORD,
        'HOST':            DATABASE_HOST,
        'PORT':            '53306',
        'ATOMIC_REQUESTS': True
        }
    }
