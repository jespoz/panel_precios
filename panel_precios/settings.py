import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '5^25wmn2ltspg_g(8goxn-u5fs00ppperb&68x#(xr3o_yxv1w'

DEBUG = True

ALLOWED_HOSTS = ['*', '192.168.12.53']


from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('panel_app:login')
LOGIN_REDIRECT_URL = reverse_lazy('panel_app:general')
LOGOUT_URL = reverse_lazy('panel_app:logout')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'apps.maestros',
    'apps.panel',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'panel_precios.urls'

WSGI_APPLICATION = 'panel_precios.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.oracle',
    #     'NAME': 'xe',
    #     'USER': 'panel_precios',
    #     'PASSWORD': 'panel_precios',
    #     'HOST': '192.168.12.53',
    #     'PORT': '1521',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'panel_precios',
        'USER': 'panel_precios',
        'PASSWORD': 'panel_precios',
        'HOST': '192.168.69.76',
        'PORT': '5432',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.oracle',
    #     'NAME': 'xe',
    #     'USER': 'panel_precios',
    #     'PASSWORD': 'panel_precios',
    #     'HOST': 'localhost',
    #     'PORT': '1521',
    # }
}

LANGUAGE_CODE = 'es-CL'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]