from app.db import db
from sqlalchemy.dialects.postgresql import TIMESTAMP, INTEGER, VARCHAR
from pprint import pprint
from sqlalchemy import text

class ArticleUrls(db.Model):
  __bind_key__ = 'scraper'
  __tablename__ = 'article_urls'

  id = db.Column(INTEGER, primary_key=True)
  title_url = db.Column(VARCHAR)


class Instances(db.Model):
  __bind_key__ = 'scraper'
  __tablename__ = 'instances'

  id = db.Column(INTEGER, primary_key=True)
  slug_text = db.Column(VARCHAR)
  slug_url = db.Column(VARCHAR)
  title_url = db.Column(VARCHAR)
  title_text = db.Column(VARCHAR)
  teaser_text = db.Column(VARCHAR)
  classes = db.Column(VARCHAR)
  article_id = db.Column(INTEGER, db.ForeignKey('article_urls.id'))
  element_type = db.Column(INTEGER)
  section_type = db.Column(INTEGER)
  story_number = db.Column(INTEGER)
  ts = db.Column(TIMESTAMP)
