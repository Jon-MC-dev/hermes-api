from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ubn9fnsnawvxiqbu:BivOg9P4Wx7EHUa1HS2z@bd2wuulpg5gelrwzim6x-mysql.services.clever-cloud.com:3306/bd2wuulpg5gelrwzim6x'
DB = SQLAlchemy(app)