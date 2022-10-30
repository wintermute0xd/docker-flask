from flask import Flask, render_template, request, url_for, redirect
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_sqlalchemy import SQLAlchemy
import os
import sys


sys.path.append(os.getcwd() + '.')

db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_name = os.environ['DB_NAME']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + db_user + \
                                        ':' + db_pass + \
                                        '@' + db_host + \
                                        ':' + db_port + \
                                        '/' + db_name

db = SQLAlchemy(app)

# tell app it's behind proxy
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def index_page():
    return "<h1>Hello, World!</h1>"

@app.route("/app")
def app_page():
    return "<h1>Flask app here</h1>"

import models
@app.route('/<int:city_id>/')
def city(city_id):
    city = models.City.query.get_or_404(city_id)
    #return render_template('student.html', student=student)
    return "<h1> " + city.cityname + "</h1>"
