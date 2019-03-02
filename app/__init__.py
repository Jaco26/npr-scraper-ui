import os
from flask import Flask, abort, jsonify
from werkzeug.exceptions import HTTPException

from .utils.app_wrappers import JsonApp, ApiFlask


def create_app():
  app = JsonApp(ApiFlask(__name__))
  app.config.from_object(os.environ['APP_SETTINGS'])

  @app.route("/")
  @app.route("/<name>")
  def index(name=None):
    return "<h1>Hello {} from Flask!</h1>".format(f"{name}," if name else "")

  return app
  