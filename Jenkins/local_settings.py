# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8zin0s2&$tok6)^8y6pn5#&a8)bht$$im%_6%^k81e_6_o^*da'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_app_1',
        'USER': 'phillip',
        'PASSWORD': 'Letrab05',
        'HOST': 'localhost'
    }
}