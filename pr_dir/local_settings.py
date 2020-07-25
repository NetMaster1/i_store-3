SECRET_KEY = '9=mm!b69r4d+*5-p)xd_47ei6-np82s(9ba4&#6z+bulph!ojv'

DEBUG = False

ALLOWED_HOSTS = ['178.128.154.158', 'www.evvy.ru', 'evvy.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'i_store_4',
        'USER': 'i_store_4_admin',
        'PASSWORD' : 'ylhio65v',
        'HOST': 'localhost'
    }
}

EMAIL_HOST= 'smtp.yandex.ru' #smtp.gmail.com
EMAIL_PORT= 587
EMAIL_HOST_USER='79200711112@yandex.ru'
EMAIL_HOST_PASSWORD = '39aZifol_01'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
