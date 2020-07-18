# -*- coding: utf-8 -*-
import os

 
class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    WEIHUB_ARTICLE_PER_PAGE = 20
    WEIHUB_ACCOUNT_PER_PAGE = 15


    # 微信
    AppSecret = os.getenv("AppSecret", "")
    AppID = os.getenv("AppID", "")


class DevelopmentConfig(BaseConfig):

    # SQLALCHEMY_ECHO = True
    # PROFILE=True
    SQLALCHEMY_RECORD_QUERIES = True
    # slow database query threshold (in seconds)
    DATABASE_QUERY_TIMEOUT = 0.5


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'staging': StagingConfig
 }
