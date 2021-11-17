from flask import Flask
from config import config_options
from .extensions import *
from dotenv import load_dotenv

load_dotenv()

# flask app factory
def create_app(config_name):
    app = Flask(__name__)

    # add config
    app.config.from_object(config_options[config_name])

    # instantiate extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt_.init_app(app)
    migrate.init_app(app, db=db)

    # TODO: register blueprints
    from .donate import donor
    
    app.register_blueprint(donor, url_prefix='/donor')

    return app
