from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

ma = Marshmallow()
db = SQLAlchemy()
bcrypt_ = Bcrypt()
migrate = Migrate()
