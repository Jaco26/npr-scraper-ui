from datetime import datetime, date, timedelta

from flask import Blueprint, abort, current_app
from app.utils.decorators import with_res

from app.queries import query
# from app.db import execute


res_api = Blueprint('res_api', __name__)

@res_api.route("/")
@with_res
def index(res):
  try:
  
    results = query.between_ts('2018-10-1', '2018-10-7', 'slug_text, title_text')
    res.message = "We got em!"
    res.set_results(results)
  except BaseException as e:
    res.clear()
    res.errors.append("Something went wrong: {}".format(e))
    res.status = 401
  finally:
    return res.json()