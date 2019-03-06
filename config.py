import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = os.environ['SECRET_KEY']
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_BINDS = {
    'scraper': os.environ['SCRAPER_DATABASE_URI'],
    'processed': os.environ['PROCESSED_DATABASE_URI'],
  }
  

class ProductionConfig(Config):
  DEBUG = False


class DevelopmentConfig(Config):
  DEBUG = True
  PROPAGATE_EXCEPTIONS = True


