from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, default_exceptions
from app.utils.decorators import ApiResult

class ApiFlask(Flask):
  def make_response(self, rv):
    if isinstance(rv, ApiResult):
      return rv.to_response()
    return Flask.make_response(self, rv)


def JsonApp(app):
  def error_handling(error):
    print('THERE WAS AN ERROR' * 2,error)
    if isinstance(error, HTTPException):
      result = {
        'code': error.code,
        'description': error.description,
        'message': str(error),
      }
    else:
      result = {
        'code': 500,
        'description': error.description,
        'message': str(error),
      }
    resp = jsonify(result)
    resp.status_code = result['code']
    print(resp.status)
    return resp

  for code in default_exceptions.keys():
    app.register_error_handler(code, error_handling)
  
  return app