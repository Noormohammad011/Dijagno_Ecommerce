import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_ecommerce',
        'USER': 'Noor011007',
        'PASSWORD': 'nayan011',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
