import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = os.environ['SECRET_KEY']
  

class ProductionConfig(Config):
  DEBUG = False


class DevelopmentConfig(Config):
  PROCESSED_DATABASE_URI = os.environ['PROCESSED_DATABASE_URI']
  SCRAPER_DATABASE_URI = os.environ['SCRAPER_DATABASE_URI']


