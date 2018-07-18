import os

class Config:

    pjdir = os.path.abspath(os.path.dirname(__file__))
    debug = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pjdir, 'static/data/data_register.sqlite')
    SECRET_KEY = b'textXXX'

