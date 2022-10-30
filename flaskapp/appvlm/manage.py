import sys
import os

# add folder to system path (prevents import error)
sys.path.append(os.getcwd() + '/..')
sys.path.append(os.getcwd() + '.')

import app
from app import db, app as appl
from models import *

# create table in flaskdb
with appl.app_context():
    db.create_all()
    db.session.commit()

# create first record in db
with appl.app_context():
    city = City(
        cityname = 'Nova Kakhovka',
        country = 'Ukraine',
        apicode = 23423)
    db.session.add(city)
    db.session.commit()
