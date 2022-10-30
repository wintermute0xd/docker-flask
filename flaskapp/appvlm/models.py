import os
import sys
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
sys.path.append(os.getcwd() + '.')
import app

db = app.db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cityname = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    apicode = db.Column(db.Integer, unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<City {self.cityname}>'