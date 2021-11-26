# 设置相关


"""
Django settings for bookmanager project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# import os    # 早期dirs列表设置模板路径用os.path.join()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# print(__file__)
# print(Path(__file__))
# print(Path(__file__).resolve())                            # 这三个输出结果均是 F:\Django\bookmanager\bookmanager\settings.py
# print(Path(__file__).resolve().parent)                     # F:\Django\bookmanager\bookmanager
# print(BASE_DIR)                                            # F:\Django\bookmanager
# 早期版本如下
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 其中__file__表示本文件setting.py文件名
# abspath(__file__)获取本文件绝对路径 F:\Django\bookmanager\bookmanager\settings.py
# dirname获取本文件所在文件夹(目录)路径 F:\Django\bookmanager\bookmanager 即获取父级目录
# 外层dirname再取上上级文件夹路径 F:\Django\bookmanager 即是BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v928^-_cr7+h06j=n$12*d(vx3vho6)-e-x&-xev(7*6a%u+e!'

# 开发者调试用，部署上线后则改为False
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False


# 允许访问后端的主机列表，默认为空仅支持本机访问
# 安全机制：只能以列举的主机进行访问
# 改变允许方式：加入ip或者域名
# 此时默认的localhost和127.0.0.1访问需要命令行添加参数访问 python manage.py runserver 127.0.0.1:8000
ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1',
                 '192.168.0.103',
                 ]


# Application definition
# 安装注册子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',            # session 已注册
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'book',                           # 直接写子应用名
    'book.apps.BookConfig',
    'pay.apps.PayConfig',               # 本质还是pay.apps.PayConfig  Django启动应用读取的是每个app的Appconfig
    'login.apps.LoginConfig',

]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',               # Django自带session中间件
    'django.middleware.common.CommonMiddleware',
    # Django默认开启了CSRF防护，会对POST等请求方式进行CSRF防护验证，在测试时可以关闭CSRF防护机制
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 注册中间件
    # 'book.middleware.simple_middleware',
    # 'book.middleware.simple_middleware2',

]


# settings.py文件中，可以设置session数据的存储方式如下
# Django对session的默认存储方式，可不写
# SESSION_ENGINE='django.contrib.sessions.backends.db'
# 设置为本地缓存：储存在本机内存中，如果丢失则不能找回，比数据库的方式读写更快
# SESSION_ENGINE='django.contrib.sessions.backends.cache'
# 设置为混合存储：优先从本机内存中存取，如果没有则从数据库中存取
# SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
# 设置为redis存储：以后session不再保存在系统django_session表中，而是保存在redis库
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",                    # 去找中间件
        # "LOCATION": "redis://127.0.0.1:6379/1",                      # 本机redis的1号库
        "LOCATION": "redis://192.168.94.131:6379/1",                   # 远程redis的1号库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# 此工程的URL配置入口，默认是工程名.urls  可修改但一般不改
ROOT_URLCONF = 'bookmanager.urls'


# 和模板相关的配置信息
TEMPLATES = [
    {
        # 修改为jinja2模板引擎
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # dirs列表设置模板路径
        'DIRS': [BASE_DIR / 'template'],
        # 'DIRS': [os.path.join(BASE_DIR, 'tempalte')],          # 这样设置需要导入os模块(早期版本)
        'APP_DIRS': True,
        'OPTIONS': {
            # 默认的，可不添加
            # 'environment': 'jinja2.Environment',
            # 指定jinja2的环境，在哪创建就写对应路径
            # 'environment': 'book.jinja2_env.environment',            # 在book应用里
            'environment': 'jinja2_env.environment',                   # 在工程里
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },

    {
        # 默认模板引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],
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


WSGI_APPLICATION = 'bookmanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# sqlite是一个嵌入式小型关系型数据库,主要是在移动端使用
# 中型数据库：mysql(甲骨文) sqlserver(微软)
# 大型数据库：oracle DB2
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',           # BASE_DIR是此工程路径，与'db.sqlite3'拼接即是数据库sqlite3的路径

        'ENGINE': 'django.db.backends.mysql',           # 指定数据库引擎为mysql
        'HOST':'192.168.94.131',
        'PORT':'3306',
        'USER':'huangzhen',
        'PASSWORD':'root',
        'NAME': 'bookmanage',            # 指定数据库名
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# 语言设置
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# 时区
# TIME_ZONE = 'UTC'    # 格林尼治时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# Django是通过STATIC_URL区分动态资源和静态资源
# Django认定：请求资源http://ip:port + STATIC_URL + 文件名 为静态资源
# 即STATIC_URL决定是否是静态资源
STATIC_URL = '/static/'

# 静态文件路由，告知系统静态文件路径
STATICFILES_DIRS = [
    BASE_DIR / 'static',             # os.path.join(BASE_DIR, 'static')
]



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
