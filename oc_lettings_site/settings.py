import os
import sentry_sdk
import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("OC_LETTINGS_DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("OC_LETTINGS_DEBUG", "").lower() == "true"
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.getenv("OC_LETTINGS_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# SECURITY WARNING: define the correct CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = os.getenv("OC_LETTINGS_CSRF_TRUSTED_ORIGINS",
                                 "http://localhost,http://127.0.0.1").split(",")

# Retrieve Sentry DSN from environment variables
SENTRY_DSN = os.getenv("OC_LETTINGS_SENTRY_DSN")

# Retrieve Sentry environment
SENTRY_ENV = os.getenv("OC_LETTINGS_SENTRY_ENV")

sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    environment=SENTRY_ENV
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'lettings.apps.LettingsConfig',  # The "lettings" app
    'profiles.apps.ProfilesConfig',  # The "profiles" app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static", ]

# Directory for log files
LOGGING_DIR = os.path.join(BASE_DIR, "logging")

# Create the directory if it doesn't exist
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

# Generate logging file name
today = datetime.datetime.now().strftime("%Y-%m-%d")
LOGGING_FILE = os.path.join(LOGGING_DIR, f"{today}.log")

# Handlers manage the destination and format of logs
LOGGING = {
    "version": 1,  # Logging configuration version
    "disable_existing_loggers": False,  # Do not disable existing loggers
    # Formatters define the format of log messages
    "formatters": {
        "standard": {
            "format": "%(levelname)-8s %(asctime)s %(module)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    # Handlers manage the destination and format of logs
    "handlers": {
        "sentry": {
            "level": "WARNING",  # Log level for Sentry
            "class": "sentry_sdk.integrations.logging.EventHandler",
        },
        "console": {
            "class": "logging.StreamHandler",  # Output logs to console
            "formatter": "standard",  # Use the standard formatter
        },
        "file": {
            "level": "INFO",  # Log level for file
            "class": "logging.FileHandler",  # Handler for writing to a file
            "filename": LOGGING_FILE,  # Path to the log file
            "formatter": "standard",  # Use the standard formatter
        },
    },
    # Loggers specify handlers and log level
    "loggers": {
        "django": {
            "handlers": [
                "sentry",
                "console",
                "file",
            ],  # Handlers used by this logger
            "level": "WARNING",  # Log level for Django
            "propagate": True,  # Propagate logs to parent loggers
        },
        "lettings": {
            "handlers": ["sentry", "console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "profiles": {
            "handlers": ["sentry", "console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "oc_lettings_site": {
            "handlers": ["sentry", "console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
