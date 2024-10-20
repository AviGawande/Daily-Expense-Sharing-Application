from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from waitress import serve

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

from routes import *

# def run_app():
#     if app.config['DEBUG']:
#         app.run(debug=True, use_reloader=False)
#     else:
#         serve(app, host='0.0.0.0', port=5000)

if __name__ == '__main__':
       app.run(debug=True)