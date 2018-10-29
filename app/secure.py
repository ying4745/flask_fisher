# ! /usr/bin/env python
# ! -*-coding:utf-8 -*-

__author__ = '左岸'

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:ying4745@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'This is a zuoan de tian kong'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'yanwei4682@qq.com'
MAIL_PASSWORD = 'bkxhfkyzmcgrbjfhhawk'