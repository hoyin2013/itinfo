# -*- coding:utf-8 -*-
"""
Django settings for itinfo project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')vvnuab2hcg0-aji_avqkiu^mcu3cf9&nk6(j0#l2g83jy9-@o'

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
    'grappelli',
    'portmap',
    'oportmap',
    'appinfo',
    'ipresource',
    'dbinfo',
    'odbinfo',
    'issues',
    'addressbook',
    'shortcut',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'itinfo.urls'

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

WSGI_APPLICATION = 'itinfo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = dict(default={
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'itinfo',
    'USER': 'root',
    'PASSWORD': 'fdsafdsa',
    'HOST': '192.168.99.100',
    'PORT': '3306',
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    }
})


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
HERE = os.path.dirname(os.path.dirname(__file__))
# 存放上传文件的目录
MEDIA_ROOT = os.path.join(HERE, './uploads/').replace('\\', '/')
# 访问上传文件目录的uri路径
MEDIA_URL = "/uploads/"
# 执行命令python manage.py collectstatic 之后静态文件将要复制到的目录，这个目录只有在运行collectstatic时候才会用到
STATIC_ROOT = os.path.join(HERE, './static/grappelli').replace('\\', '/')

# 模版中使用的静态文件指向路径
STATICFILES_DIRS = (os.path.join(HERE, './static/').replace('\\', '/'),)
# 调用方式举例
# {% load staticfiles %}
# <img src="{% static "my_app/myexample.jpg" %}" alt="My image"/>

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

GRAPPELLI_ADMIN_TITLE = '中汇支付运维综合管理系统'
