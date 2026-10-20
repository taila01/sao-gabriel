import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# O ambiente da hospedagem tem prioridade sobre o arquivo local.
environ.Env.read_env(BASE_DIR / ".env", overwrite=False)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6x)t22)01f#v8m^la2(l58xtx_af(dh^%%nok@#%!k!wcyad$%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "False" if os.environ.get("VERCEL") else "True").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,sao-gabriel-blue.vercel.app"
    ).split(",")
    if host.strip()
]
if os.environ.get("VERCEL_URL"):
    ALLOWED_HOSTS.append(os.environ["VERCEL_URL"])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social_django',
     
    'users',
    'product',
    'payment',
    'app_admin',
    'store',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'payment': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Define o nível para exibir todos os logs (incluindo ERROR)
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO', # Manter logs padrão do Django
            'propagate': True,
        },
    },
}
#api logingoogle
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2', 
    'django.contrib.auth.backends.ModelBackend',  
)

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'store:index'
LOGOUT_REDIRECT_URL = 'users:login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware'
]

ROOT_URLCONF = 'sao_gabriel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'sao_gabriel.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "sao_gabriel.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME", "bd_coffee"),
        "USER": os.environ.get("DB_USER", "taila"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "3306"),
        "OPTIONS": {"use_pure": True},
    }
}

# Aiven exige TLS; valide a CA e a identidade do servidor.
_db_ssl_ca = os.environ.get("DB_SSL_CA")
if not _db_ssl_ca and (BASE_DIR / "ca.pem").is_file():
    _db_ssl_ca = str(BASE_DIR / "ca.pem")
if _db_ssl_ca:
    DATABASES["default"]["OPTIONS"].update({
        "ssl_ca": str(BASE_DIR / _db_ssl_ca),
        "ssl_disabled": False,
        "ssl_verify_cert": True,
        "ssl_verify_identity": True,
    })


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Configurações do Mercado Pago (Sandbox/Teste) ---
MP_ACCESS_TOKEN = 'APP_USR-2201546978636815-111017-c7629d7e22017f3b3ad4ca670d35e378-2979950899'