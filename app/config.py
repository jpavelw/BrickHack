__author__ = 'codnee'

import os

"""
    See all security configurations available at:
    https://pythonhosted.org/Flask-Security/configuration.html
"""


class SecurityConfig(object):
    SECURITY_URL_PREFIX = '/user'
    SECRET_KEY = 'Meh'
    #SECURITY_PASSWORD_HASH = 'bcrypt'
    #SECURITY_PASSWORD_SALT = ''


class SecurityFeatures(object):
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = False
    SECURITY_PASSWORDLESS = False
    SECURITY_CHANGEABLE = True


class EmailConfig(object):
    MAIL_SERVER = 'smtp.something.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''


class SecurityEmailConfig(object):
    SECURITY_EMAIL_SENDER = 'no-responda@algo.com'


class HerokuConfig(SecurityConfig, SecurityFeatures, EmailConfig):
    DATABASE_URL = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = True

