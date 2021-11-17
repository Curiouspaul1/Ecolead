from enum import unique
from main.extensions import db
from datetime import datetime as dt

# User Models

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(200))
    sign_up_date = db.Column(db.Date, default=dt.utcnow())
    is_verified = db.Column(db.Boolean, default=False)
    # TODO: add more fields as need be


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.Text)
    donate_link = db.Column(db.String(200))
    has_donate_link = db.Column(db.Boolean, default=False)
    sign_up_date = db.Column(db.Date, default=dt.utcnow())

    # TODO: add more fields as need be

