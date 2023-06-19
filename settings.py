from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lip5d8lk++338i_!9r8)%ilegyo5$27!$y8g-q*oore8v7y1i6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# CORS

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://localhost:4173",
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

# Application definition

INSTALLED_APPS = [
    "daphne",
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.import_export",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    'mdeditor',
    "drf_yasg",
    "rest_framework_simplejwt",
    "api",
    "api.docs",
    "api.users",
    "api.url_shortener"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates"
        ],
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

ASGI_APPLICATION = "backend.asgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_USER_MODEL = 'users.User'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# REST_FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}


# Documentation


SWAGGER_SETTINGS = {
    "DEFAULT_MODEL_RENDERING": "example",
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': True,
    'HIDE_HOSTNAME': True,
    'PATH_IN_MIDDLE': True,
    "REQUIRED_PROPS_FIRST": True,
    'FETCH_SCHEMA_WITH_QUERY': True
}


#  Md-editor

MDEDITOR_CONFIGS = {
    'default': {
        'width': '90% ',  # Custom edit box width
        'height': 500,  # Custom edit box height
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
        # image upload format type
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        'image_folder': 'editor',  # image save the folder name
        'theme': 'dark',  # edit box theme, dark / default
        'preview_theme': 'dark',  # Preview area theme, dark / default
        'editor_theme': 'dark',  # edit area theme, pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement
        'emoji': True,  # whether to open the expression function
        'tex': True,  # whether to open the tex chart function
        'flow_chart': True,  # whether to open the flow chart function
        'sequence': True,  # Whether to open the sequence diagram function
        'watch': True,  # Live preview
        'lineWrapping': False,  # lineWrapping
        'lineNumbers': False,  # lineNumbers
        'language': 'en'  # zh / en / es
    }

}

# Admin

UNFOLD = {
    # "SITE_TITLE": "Hello World",
    "SITE_HEADER": "DRF Admin",
    "SITE_ICON": lambda request: static("favicon.png"),
    "SITE_SYMBOL": "speed",
    "LOGIN": {
        "image": lambda r: static("login.jpg"),
    },
    "SIDEBAR": {
        "show_search": True,
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": True,  # Top border
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        # "badge": "sample_app.badge_callback",
                    },
                    {
                        "title": _("Docs"),
                        "icon": "newspaper",
                        "link": reverse_lazy("admin:docs_postgroup_changelist"),
                    },
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                ],
            },
        ],
    },
    "TABS": [
        {
            "models": [
                "users.user",
            ],
            "items": [
                {
                    "title": _("Users"),
                    "link": reverse_lazy("admin:users_user_changelist"),
                },
                {
                    "title": _("Profiles"),
                    "link": reverse_lazy("admin:users_userprofile_changelist"),
                },
            ],
        },
        {
            "models": [
                "users.userprofile",
            ],
            "items": [
                {
                    "title": _("Users"),
                    "link": reverse_lazy("admin:users_user_changelist"),
                },
                {
                    "title": _("Profiles"),
                    "link": reverse_lazy("admin:users_userprofile_changelist"),
                },
            ],
        },
        {
            "models": [
                "docs.postgroup",
            ],
            "items": [
                {
                    "title": _("Posts Groups"),
                    "link": reverse_lazy("admin:docs_postgroup_changelist"),
                },
                {
                    "title": _("Posts"),
                    "link": reverse_lazy("admin:docs_post_changelist"),
                },
                {
                    "title": _("Docs Settings"),
                    "link": reverse_lazy("admin:docs_docssetting_changelist"),
                },
            ],
        },
        {
            "models": [
                "docs.post",
            ],
            "items": [
                {
                    "title": _("Posts Groups"),
                    "link": reverse_lazy("admin:docs_postgroup_changelist"),
                },
                {
                    "title": _("Posts"),
                    "link": reverse_lazy("admin:docs_post_changelist"),
                },
                {
                    "title": _("Docs Settings"),
                    "link": reverse_lazy("admin:docs_docssetting_changelist"),
                },
            ],
        },
        {
            "models": [
                "docs.docssetting",
            ],
            "items": [
                {
                    "title": _("Posts Groups"),
                    "link": reverse_lazy("admin:docs_postgroup_changelist"),
                },
                {
                    "title": _("Posts"),
                    "link": reverse_lazy("admin:docs_post_changelist"),
                },
                {
                    "title": _("Docs Settings"),
                    "link": reverse_lazy("admin:docs_docssetting_changelist"),
                },
            ],
        },
    ],
}


def badge_callback(request):
    return 3
