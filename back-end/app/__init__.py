from flask import Flask

from config import config
from .models import db


def create_app(config_name):
    app = Flask(__name__)
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
