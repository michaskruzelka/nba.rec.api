import os

from flask import Flask
from flask_cors import CORS

from api.config import config


def create_app():
    app = Flask(__name__)
    CORS(app)
    env = os.environ.get("FLASK_ENV", "dev")
    app.config.from_object(config[env])
    return app
