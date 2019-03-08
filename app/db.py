import os
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool
from dotenv import load_dotenv

from flask import g

load_dotenv()

# DB_URI = os.environ.get("SCRAPER_DATABASE_URI")
DB_URI = os.environ.get("PROCESSED_DATABASE_URI")

URI_ITEMS = DB_URI[DB_URI.index('//') + 2:].split(':')

pool = ThreadedConnectionPool(
  minconn=1, 
  maxconn=20,
  user=URI_ITEMS[0],
  password=URI_ITEMS[1].split('@')[0],
  host=URI_ITEMS[1].split('@')[1],
  port=URI_ITEMS[2].split('/')[0],
  database=URI_ITEMS[2].split('/')[1]
)

def get_db_conn():
  if 'db' not in g:
    g.db = pool.getconn()
  return g.db

def execute(sql_text, values=()):
  with get_db_conn() as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as c:
      c.execute(sql_text, values)
      result = c.fetchall()
  return result
      

def return_conn(x):
  db = g.pop('db', None)
  if db:
    pool.putconn(db)

def init_app(app):
  app.teardown_appcontext(return_conn)

