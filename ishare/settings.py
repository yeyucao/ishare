"""
Django settings for ishare project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7=2y6u_5e=3mx0ut5hct!4t)g7gjy@7j_r$-(jv0&#n%v+@p=!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 维护期间阻止用户登录后台产生新的数据
UPGRADING = True

pymysql.install_as_MySQLdb()

ALLOWED_HOSTS = [
    "blog.lujianxin.com",
    "*"
]

SERVER = 'http://{}'.format(ALLOWED_HOSTS[0])

# Application definition
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

INSTALLED_APPS.extend([
    # 主要业务模块
    'ishare',
    'blog',
])

INSTALLED_APPS.extend([
    # 功能拓展模块
    'crispy_forms',
    'reversion',
    'DjangoUeditor',
])

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 以下是自定义中间件
    'blog.my_middlewares.AllMethodSupportMiddleware',
    # 'blog.my_middlewares.VisitCountMiddleware',
    # 以下是开启缓存中间件
    # 'django.middleware.cache.CacheMiddleware',
]

ROOT_URLCONF = 'ishare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',

                # 以下为自定义模板上下文
                'blog.my_context_processors.site',
                'blog.my_context_processors.cats',
                'blog.my_context_processors.site_count',
                'blog.my_context_processors.most_read',
                'blog.my_context_processors.notice',
                'blog.my_context_processors.recommend',
                'blog.my_context_processors.live_re',
                'blog.my_context_processors.links',
                # 'blog.my_context_processors.valine',
            ],
        },
    },
]

WSGI_APPLICATION = 'ishare.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.mysql',
#     #     'NAME': 'ishare',
#     #     'USER': 'root',
#     #     'PASSWORD': 'lujianxin.com',
#     #     'HOST': 'lujianxin.com',
#     #     'PORT': '3306',
#     # }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dxf',
        'USER': 'dxf',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'blog.UserAccount'
AUTHENTICATION_BACKENDS = (
    'ishare.auth.EmailAuthBackend',
)

# 云评论插件的账户信息
LIVE_RE = {
    'data_id': 'city',
    'data_uid': 'lujianxin.com',
}

# valine 评论系统账户
VALINE = {
    'appId': 'lujianxin.com',
    'appKey': 'lujianxin.com',
    'region': 'cn',  # 节点 cn 或 us
    'notify': 'true',  # 邮件提醒
    'verify': 'true',  # 验证码
    'avatar': 'monsterid',  # 访客头像
    'placeholder': '我有话要说...',
    # meta: ['nick', 'mail', 'link'],
    'pageSize': 10,  # 每页展示评论数
    'lang': 'zh-cn',  # 语言， 参考i18n
    'visitor': 'true',  # 文章访问量统计开启或关闭
    'highlight': 'true',  # 代码高亮
    'avatarForce': 'false',  # 强制拉取新头像
    'recordIP': 'true',  # 是否记录访客ip
    # serverURLs: '{{ VALINE.serverURLs }}',  // 国内自定义域名#
}

# 站点信息
SITE = {
    'team': 'lujianxin.com',
    'dns': ALLOWED_HOSTS[0],
    'host': 'http://{}'.format(ALLOWED_HOSTS[0]),
    'name': '信息展示',
    'me': 'https://lujianxin.com',
    'author': "Jeyrce.Lu",
    'email': {
        'jubao': 'admin@imseek.cn',
        'tougao': 'admin@imseek.cn',
        'support': 'admin@imseek.cn',
        'me': 'jeyrce@gmail.com',
    },
    # 工信部备案号
    'icp': {
        'code': '浙ICP备18053740号-2',
        'link': 'http://beian.miit.gov.cn/',
    },
    # 公安部备案号
    'psb': {
        'code': '浙公网安备33010802010917号',
        'link': 'http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010802010917',
    },
    # 各种搜索引擎验证码
    'search_engine_metas': {
        'baidu-site-verification': '5amdMOKaXx',
        'google-site-verification': 'C2ujkHLAjxkyD2SXrnXNeoZum0YsZcl832GvR3XBTw4',
        '360-site-verification': '8a43aac6e4ecbfb7849b61c40cdebd76',
        'shenma-site-verification': '61038a23c3906f69d8ec598c57a5988c_1556268317',
        'sogou_site_verification': '7LJQRWpzdw',
        'msvalidate.01': '725274B06FEC1DAE34DA835E37A6D5D5',
    },
    'UPGRADING': UPGRADING,
}

# 缓存配置
#########
# CACHE #
#########

CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 180
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
    'one': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
    'two': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
    'three': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
    'four': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

############
# SESSIONS #
############

# Cache to store session data if using the cache session backend.
SESSION_CACHE_ALIAS = 'default'
# Cookie name. This can be whatever you want.
SESSION_COOKIE_NAME = 'sessionid'
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60
# The path of the session cookie.
SESSION_COOKIE_PATH = '/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = not DEBUG
# class to serialize session data
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
# 基于cache的缓存: redis
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
DJANGO_REDIS_IGNORE_EXCEPTIONS = True  # 忽略异常

LOGOUT_REDIRECT_URL = '/'
CSRF_USE_SESSIONS = True

# celery配置
CELERY_BROKER_URL = BROKER_URL = 'redis://:lujianxin.com@127.0.0.1:6379/2'
CELERY_RESULT_BACKEND = 'redis://:lujianxin.com@127.0.0.1:6379/3'
CELERY_CACHE_BACKEND = 'django-cache'
BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': 3600,
    'fanout_prefix': True,
}

# ----------本站系统所用email配置----------
SERVER_EMAIL = 'admin@imseek.cn'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465

EMAIL_USE_LOCALTIME = False

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'admin@imseek.cn'
EMAIL_HOST_PASSWORD = 'lujianxin.com'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None

DEFAULT_FROM_EMAIL = 'admin@imseek.cn'
EMAIL_SUBJECT_PREFIX = '[信息展示]'

LIST_INFO = {
    'page_size': 30,
    'A': """其实我一直想写点什么，现在终于着手试一下。曾经也算个文艺青年，经过生活琐事的稀释，
    现在也不剩多少墨水了。单独开出这个栏目，希望重拾我的文学梦想。
    """,
    'B': """如果有人与我们分享过一个夏季，我们的记忆就会在生命中相互呼唤，
    如果我们曾经怀着相同的理想并肩前行过一段岁月，到了最后会不会在彼此的记忆中植满百合？
    """,
    'tag': '此标签检索到以下结果，如果没有你想找的，也可点击右上角进行站内搜索。',
}

# ------------simpleui配置

SIMPLEUI_HOME_TITLE = '后台首页'
SIMPLEUI_LOGO = '/static/image/favicon.ico'
SIMPLEUI_HOME_INFO = True
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_HOME_ACTION = True
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_LOGIN_PARTICLES = False  # 关闭登录页粒子动画
SIMPLEUI_ANALYSIS = False
SIMPLEUI_CONFIG = {
    'system_keep': True,
    # 'menus': [{
    #     'name': 'Simpleui',
    #     'icon': 'fas fa-code',
    #     'url': 'https://gitee.com/tompeppa/simpleui'
    # }, {
    #     'app': 'auth',
    #     'name': '权限认证',
    #     'icon': 'fas fa-user-shield',
    #     'models': [{
    #         'name': '用户',
    #         'icon': 'fa fa-user',
    #         'url': 'auth/user/'
    #     }]
    # }, {
    #     'name': '测试',
    #     'icon': 'fa fa-file',
    #     'models': [{
    #         'name': 'Baidu',
    #         'url': 'http://baidu.com',
    #         'icon': 'far fa-surprise'
    #     }, {
    #         'name': '内网穿透',
    #         'url': 'https://www.wezoz.com',
    #         'icon': 'fab fa-github'
    #     }]
    # }]
}

# ===========>Feed<===========
SITE_ID = 7

# ==========>logging<==========
LOGGING_PATH = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_PATH): os.mkdir(LOGGING_PATH)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(levelname)s][%(asctime)s] [%(filename)s] [%(module)s.%(funcName)s:%(lineno)d]-%(message)s'},
        # 简单格式
        'simple': {
            'format': '%(levelname)s %(funcName)s %(message)s'
        },
    },
    # 过滤
    'filters': {
        # 暂无过滤
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_PATH, 'ishare.log'),
            'maxBytes': 1024 * 1024 * 10,  # 文件大小 10M
            'backupCount': 10,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_PATH, 'error.log'),
            'maxBytes': 1024 * 1024 * 10,  # 文件大小
            'backupCount': 10,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_PATH, 'info.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False,  # 是否轮转
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'