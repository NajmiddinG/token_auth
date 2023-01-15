from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-)#mt(djz5#j238qjx-y9u=3isabt+pzj)=k84ef+godz=j5v*k'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','rest_framework','rest_framework.authtoken','drf_spectacular','auth_app',]
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware',]
ROOT_URLCONF = 'main.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [],'APP_DIRS': True,'OPTIONS': {'context_processors': ['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages',],},},]
WSGI_APPLICATION = 'main.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3',}}
AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'auth_app.User'
REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',}
SPECTACULAR_SETTINGS = {'COMPONENT_SPLIT_REQUEST': True,}