from datetime import datetime, date, timedelta
from flask import Blueprint, abort, current_app
from app.utils.decorators import with_res
from app.models.instances import Instances

res_api = Blueprint('res_api', __name__)

@res_api.route("/")
@res_api.route("/<d1>/<d2>")
@with_res
def index(res, d1=None, d2=None):
  try:
    results = Instances.ts_between('2018-10-1', '2018-10-7')
    res.message = "We got em!"
    res.set_results([x.to_dict() for x in results])
  except BaseException as e:
    res.clear()
    res.errors.append("Something went wrong: {}".format(e))
    res.status = 401
  finally:
    return res.json()