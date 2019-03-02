import functools
from flask import jsonify

class ApiResult(object):
  def __init__(self, data={}, info=[], errors=[], status=200):
    self.data = data
    self.info = info
    self.errors = errors
    self.status = status

  def to_response(self):
    return jsonify(
      data=self.data,
      errors=self.errors,
      info=self.info,
      status=self.status,
    )

def with_res(func):
  @functools.wraps(func)
  def func_wrapper(*args, **kwargs):
    return func(ApiResult(), *args, **kwargs)
  return func_wrapper

