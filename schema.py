from models import *
from main.extensions import ma


class DonorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Donor

donor_schema = DonorSchema()
donors_schema = DonorSchema(many=True)
