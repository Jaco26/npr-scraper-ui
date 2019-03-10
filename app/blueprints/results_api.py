from datetime import datetime, date, timedelta
from flask import Blueprint, abort, current_app
from app.utils.decorators import with_res
from app.models.instances import Instances
# from app.queries.instances import count_slugs

res_api = Blueprint('res_api', __name__)

@res_api.route("/")
@res_api.route("/<d1>/<d2>")
@with_res
def index(res, d1='2018-10-1', d2='2018-10-7'):
  try:
    res.set_results(Instances.ts_between(d1, d2))
  except BaseException as e:
    res.clear()
    res.add_error(err=e)
    res.status = 400
  finally:
    return res.json()

@res_api.route("/slugs")
@with_res
def slugs(res):
  try:
    res.set_results(Instances.count_slug_groups())
  except BaseException as e:
    res.clear()
    res.add_error(err=e)
    res.status = 400
  finally:
    return res.json()