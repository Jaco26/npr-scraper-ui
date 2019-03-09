import os
from flask import Flask, abort, jsonify
from werkzeug.exceptions import HTTPException

from .utils.app_wrappers import JsonApp
from .blueprints.results_api import res_api
from .db import db

def create_app():
  app = JsonApp(Flask(__name__))
  app.config.from_object(os.environ['APP_SETTINGS'])

  db.init_app(app)

  app.register_blueprint(res_api, url_prefix="/api/results")

  return app
  