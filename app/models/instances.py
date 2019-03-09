from app.db import db
from sqlalchemy import func, and_
from sqlalchemy.dialects.postgresql import (
  VARCHAR, INTEGER, TIMESTAMP
)
from datetime import date, datetime

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
    return cls.query.filter(and_(cls.ts.between(d1, d2))).all()

