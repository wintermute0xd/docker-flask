from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_page():
    return "<h1>Hello, World</h1>"
