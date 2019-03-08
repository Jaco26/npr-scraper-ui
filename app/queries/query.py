from datetime import datetime, date
from app.db import execute

def between_ts(d1, d2, columns):
  sql_text = """
    SELECT date_trunc('hour', ts) {} FROM instances
    WHERE ts BETWEEN %s AND %s
    ORDER BY ts;
  """.format(", " + columns,)
  return execute(sql_text, (d1, d2))
