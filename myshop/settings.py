import os
# from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g6b4c#l8&(=ygbcuypf3nra9_veu-7dnw_cotv2=a3w&6*_u66'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
    'account.apps.AccountConfig',
    # 'rosetta',
    # 'parler',
    # 'localflavor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'cart.context_processor.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en'

# LANGUAGES = (
#     ('en', _('English')),
#     ('ar', _('Arabic')),
#     ('es', _('Spanish')),
# )
#
# PARLER_LANGUAGES = {
#     None: (
#         {'code': 'en'},
#         {'code': 'ar'},
#         {'code': 'es'},
#     ),
#     'default': {
#         'fallback': 'en',
#         'hide_untranslated': False,
#     }
# }


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale/'),
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL  = '/media/'

# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT  = os.path.join(BASE_DIR, "media/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

CART_SESSION_ID = 'cart'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Braintree settings
BRAINTREE_MERCHANT_ID = 'hmkc3b6wtwqqn78y' # Merchant ID
BRAINTREE_PUBLIC_KEY = 'rb5w8dh4hf987fmg' # Public Key
BRAINTREE_PRIVATE_KEY = 'c9e16c83c04d2c3de61a2116fdd56c4f' # Private key

from braintree import Configuration, Environment

Configuration.configure(
    Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
