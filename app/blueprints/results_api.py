from flask import Blueprint, abort
from app.utils.decorators import with_res
from app.models.instances import Instances

res_api = Blueprint('res-api', __name__)

@res_api.route("/")
@with_res
def index(res):
  res.message = "There is something happening here"
  return res
