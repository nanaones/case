from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort, Response
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import os

if not os.getenv("DATABASEURI") is None:
    _dbms_uri = os.getenv("DATABASEURI")
else:
    _dbms_uri = "postgresql://postgres:8015@localhost/postgres"


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = _dbms_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
CORS(app)

