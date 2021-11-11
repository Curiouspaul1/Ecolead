from flask import Flask
from config import config_options
from .extensions import *

# flask app factory
def create_app(config_name):
    app = Flask

    # add config
    app.config.from_object(config_options[config_name])

    # instantiate extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt_.init_app(app)


    # TODO: register blueprints
    return app
