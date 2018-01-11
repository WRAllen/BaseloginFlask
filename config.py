# -*- coding:utf-8 -*-

class Config(object):

    SECRET_KEY = "Ay98Cct2oNSlnHDdTl8"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    @staticmethod
    def init_app(app):
        pass

class LastConfig(Config):
    '''
        调试
        连接数据库
    '''
    DEBUG = True
    #SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/test_one"


class TestConfig(Config):
    '''
        测试数据库
        调试
        连接数据库
    '''
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://lincox:655334linkong@localhost:3306/test_data"


config = {'default':LastConfig, 'test':TestConfig}
