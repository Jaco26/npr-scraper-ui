import os
from flask import Flask, abort, jsonify
from werkzeug.exceptions import HTTPException

from .db import db
from .utils.app_wrappers import JsonApp, ApiFlask
from .blueprints.results_api import res_api


def create_app():
  app = JsonApp(ApiFlask(__name__))
  app.config.from_object(os.environ['APP_SETTINGS'])

  db.init_app(app)

  app.register_blueprint(res_api, url_prefix="/api/results")

  return app
  