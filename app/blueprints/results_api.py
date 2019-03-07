from datetime import datetime, date, timedelta

from flask import Blueprint, abort, current_app
from app.utils.decorators import with_res
from app.db import execute


res_api = Blueprint('res_api', __name__)

@res_api.route("/")
@with_res
def index(res):
  try:
    start = datetime.now()
    sql_text = """
      SELECT date_trunc('hour', ts), slug_text, title_text FROM instances
      WHERE ts BETWEEN %s AND %s
      ORDER BY ts;
    """
    results = execute(sql_text, (date(2019, 3, 1).isoformat(), date(2019, 3, 2).isoformat()))
    res.message = "We got em!"
    res.set_results(results)
  except BaseException as e:
    res.clear()
    res.errors.append("Something went wrong: {}".format(e))
    res.status = 401
  finally:
    print(len(res.data['results']))
    end = datetime.now()
    print(end - start)
    return res.json()