from app.db import db
from sqlalchemy import func, text, and_
from sqlalchemy.dialects.postgresql import (
  VARCHAR, INTEGER, TIMESTAMP
)
from datetime import date, datetime

class ArticleInstances(db.Model):
  __tablename__ = 'article_urls'

  id = db.Column(INTEGER, primary_key=True)
  title_url = db.Column(VARCHAR)



class Instances(db.Model):
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

  def to_dict(self):
    return dict(
      id=self.id,
      slug_text=self.slug_text,
      slug_url=self.slug_url,
      title_url=self.title_url,
      title_text=self.title_text,
      teaser_text=self.teaser_text,
      classes=self.classes,
      article_id=self.article_id,
      element_type=self.element_type,
      section_type=self.section_type,
      story_number=self.story_number,
      ts=str(self.ts),
    )

  @classmethod
  def ts_between(cls, d1, d2):
    return [x.to_dict() for x in cls.query.filter(and_(cls.ts.between(d1, d2))).all()]


  @classmethod
  def count_slug_groups(cls):
    result = cls.query.with_entities(
      func.count(cls.slug_text).label("count"),
      cls.slug_text
    ).order_by(text("count desc")).group_by(cls.slug_text).all()
    return [dict(
      count=i[0], 
      slug_text=i[1]
      ) for i in result]

  
