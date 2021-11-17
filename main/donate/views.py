from . import donor
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from main import db, bcrypt_
from models import Donor
import json


@donor.post("/")
def register():
    data = request.get_json(force=True)
    new_user = Donor()
    for key, value in data.items():
        new_user.__setattr__(key, value)
        if key == "password":
            # gen password hash
            pw_hash = bcrypt_.generate_password_hash(value)
            new_user.__setattr__(
                "password_hash",
                str(pw_hash, encoding="utf-8")
            )
            pass
    db.session.add(new_user)
    try:
        db.session.commit()
        return {
            "status": "success",
            "message": "Created donor successfully",
            "data": None
        }, 201
    except IntegrityError:
        return {
            "status": "fail",
            "data": {"email": "Email already exists"}
        }, 403


@donor.get("/")
def get_donors():
    data = Donor.query.all()
    return json.dumps(data)
