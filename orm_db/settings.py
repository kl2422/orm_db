"""
Django settings for orm_db project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@t$$7urk$zw49b*y14ump4ub++gajm0exmvyof1=ffqu=as^!_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'common.apps.CommonConfig',
    'users.apps.UsersConfig',
    'school.apps.SchoolConfig',
    'polls.apps.PollsConfig',
    'employee.apps.EmployeeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'orm_db.mymiddleware.LoggerMiddleware',
]

ROOT_URLCONF = 'orm_db.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'orm_db.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'scott',       # 你要存储数据的库名，事先要创建之
        'USER': 'root',         # 数据库用户名
        'PASSWORD': '123456',     # 密码
        'HOST': 'localhost',    # 主机
        'PORT': '3306',         # 数据库使用的端口
        #'ATOMIC_REQUESTS': True,

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    }
}

# 使用的缓存别名（默认内存缓存）
SESSION_CACHE_ALIAS = 'default'

SESSION_COOKIE_AGE = 1209600 # 默认两周单位秒
SESSION_COOKIE_DOMAIN = None # session cookie域名 默认没有设置就是当前域名
SESSION_COOKIE_HTTPONLY = True # 设置session cookie是httponly
SESSION_COOKIE_NAME = 'sessionId' # session cookie的名字
SESSION_COOKIE_PATH = '/' #  session cookie的path
SESSION_COOKIE_SECURE = False # session cookie的secure
SESSION_ENGINE = 'django.contrib.sessions.backends.db' # session存贮位置默认db
# 'django.contrib.sessions.backends.db'
# 'django.contrib.sessions.backends.file'
# 'django.contrib.sessions.backends.cache'
# 'django.contrib.sessions.backends.cached_db'
# 'django.contrib.sessions.backends.signed_cookies'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False # 浏览器关闭后是否过期session，默认是False
SESSION_FILE_PATH = None #默认没有，就是选择session存储是file时设置的存储位置
# 浏览器刷新时session是否重新计算过期时间，
# 比如设置10分钟过期，那如果为True，每次刷新session都是重新计算时间，
# 如果为False就是10分钟后就过期不管你刷不刷新
SESSION_SAVE_EVERY_REQUEST = False
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer' # session序列化类型
# 'django.contrib.sessions.serializers.PickleSerializer'
# 'django.contrib.sessions.serializers.JSONSerializer'





