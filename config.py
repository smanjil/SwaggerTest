import pymysql
from flask import Flask
from flasgger import Swagger

db = pymysql.connect('localhost', 'root', '123', 'petdb')
cur = db.cursor()

app = Flask(__name__)
Swagger(app)

