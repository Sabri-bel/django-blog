"""
Django settings for codestar project.

Generated by 'django-admin startproject' using Django 4.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# The dj_database_url import is used to convert the database URL we copied from our PostgreSQL from Code Institute email into a format that Django can use to connect to an external database server.
from django.contrib.messages import constants as messages
import dj_database_url
# The code uses another method from the os module to check if the env.py file path exists. If it does, then it will be imported. If it does not exist, the env import will not be attempted so that no error will occur.
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # build a path for our subdirectory 'templates'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# This is a unique, secret, and random string that is used for cryptographic signing. That means that it ensures the integrity of the data stored
SECRET_KEY = 'django-insecure-c+ip(9r-3l$$%-^tsj6b$2v5^ejcc0c4%e!g-&(tqu@=y5*ii8'
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Application definition

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
    'crispy_bootstrap5',
    'cloudinary_storage',
    'cloudinary',
    'django_summernote',
    'blog',
    'about',
]

SITE_ID = 1  # 1 means that django can handle miltple sites from one database
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"  # use this a teplate pack
CRISPY_TEMPLATE_PACK = "bootstrap5"

# middleware  sits between the request and the response, a bit like a specialised kind of view.
# Middleware can modify a request prior to it hitting the view code and then modify the response after the view has created it.
# In the case of Whitenoise, it modifies the response to load the static files from the staticfiles directory and serve them when a user visits our site.
# Note: Middleware often needs to be loaded in a particular order. The documentation for a piece of middleware will tell you where it needs to be in the MIDDLEWARE list in settings.py.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # must be placed directly after the Django SecurityMiddleware.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'codestar.urls'

# below the code that tells django where to find templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # The DIRS key tells Django which directories to look in
        'APP_DIRS': True,  # APP_DIRS set to True, which means that Django will also look for a templates directory inside all our app directories.
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

WSGI_APPLICATION = 'codestar.wsgi.application'


# Default django database not required since there is a connection with sql postgres
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

DATABASES = {
    'default':
    # This code uses os.environ.get to get the value stored in the DATABASE_URL environment variable. The value is then parsed using dj_database_url to put it in a format that Django can use
        dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


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

ACCOUNT_EMAIL_VERIFICATION = 'none'  # Without this line, you would get Internal Server errors (code 500) during login and registration.

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success',
    messages.ERROR: 'alert-danger',
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # statifiles is automatically created from "collect statics" command
# The collectstatic needs to be run every time we add or change a CSS, JavaScript or static image file.
# Using whitenoise, Django will serve all our CSS, JavaScript and static image files from that directory

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# below a list of the trusted origins for requests. As shown, you need to add both your local development server URL domain and your production server URL domain to allow you to add blog post content from the admin dashboard.
# The subdomain is wildcarded with a *. CSRF stands for Cross-Site Request Forgery.
# CSRF_TRUSTED_ORIGINS setting ensures that the only requests allowed are ones originating from hosts in the list. That's why Django blocks access to the admin site if you don't have the correct host setting in there.
CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
    "https://*.herokuapp.com"
]
