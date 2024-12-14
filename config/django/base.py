import os
from config.env import BASE_DIR, env
from django.utils.translation import gettext_lazy as _

""" Read environment variables from .env file """
env.read_env(os.path.join(BASE_DIR, ".env"))

""" Secret Key """
SECRET_KEY = env("SECRET_KEY")

""" Debug """
DEBUG = env.bool("DJANGO_DEBUG", default=True)

""" Allowed hosts """
ALLOWED_HOSTS = ["*"]


UNFOLD = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
]


DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]


THIRD_PARTY_APPS = [
    "import_export",
    "guardian",
    "simple_history",
    "djmoney",
    "debug_toolbar",
    "easyaudit",
    "tailwind",
    "django_browser_reload",
    "neapolitan",
    "django_cotton",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.usersessions",
    "allauth.socialaccount.providers.github",
]

PROJECT_APPS = ["core", "theme"]


INSTALLED_APPS = UNFOLD + DEFAULT_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "easyaudit.middleware.easyaudit.EasyAuditMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "allauth.usersessions.middleware.UserSessionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-in"

TIME_ZONE = "Asia/kolkata"

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ("de", _("German")),
    ("en", _("English")),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


""" Custom User Model """
AUTH_USER_MODEL = "core.User"

""" Email """
from config.settings.email import *

""" UNFOLD """
from config.settings.unfold import *

""" Debug Toolbar """
from config.settings.debug_toolbar import *

""" Easy Audit """
from config.settings.audit import *

""" Tailwind CSS """
from config.settings.tailwind import *

""" AllAUth """
from config.settings.all_auth import *
