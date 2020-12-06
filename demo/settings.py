import os
# from decouple import config
# import paypalrestsdk
# from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj'
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'ckeditor',
    'ckeditor_uploader',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'demo.urls'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Creating Access Token for Sandbox
# client_id = "AXXcMRWtb1jd0IamK8OUX1Ww43lN-d0n_TK3GUpjmoyOSRirmY8k7Yc6RwvbvlZF0q0YPWYqhpRn9Y3D"
# client_secret = "EBRZkNTv8WBydmmIPfgtrkEgEUHv_td7j92LHtutj0KhyGt2OijIhoX54b9P-NP91TNks_pZ_sB3kOqF"
# # Creating an environment
# environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
# client = PayPalHttpClient(environment)
# paypalrestsdk.configure({
#   "mode": "sandbox", # sandbox or live
#   "client_id": "AXXcMRWtb1jd0IamK8OUX1Ww43lN-d0n_TK3GUpjmoyOSRirmY8k7Yc6RwvbvlZF0q0YPWYqhpRn9Y3D",
#   "client_secret": "EBRZkNTv8WBydmmIPfgtrkEgEUHv_td7j92LHtutj0KhyGt2OijIhoX54b9P-NP91TNks_pZ_sB3kOqF" })

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

SITE_ID = 1
####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

###################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
    }
}
LOGIN_REDIRECT_URL = '/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
# STRIPE_PUBLIC_KEY = 'pk_test_51HnjMQIkK8JL3mnjiTxcTDcyWr45SVWvQM15URUC8WovolQavUvLlsfdS6eBHwOcRmZkHmENH10VJCVL9BE1Ko5I00ojDJ5SnA'
# STRIPE_SECRET_KEY = 'sk_test_51HnjMQIkK8JL3mnjTw57LaWsXlbtvE3c7J1n777NPflVKHg3D9eTOmYXIhKgmcHe9UdcsM54KKXTQQlmHhJrblFk00STmBjz1O'

if ENVIRONMENT == 'production':
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
