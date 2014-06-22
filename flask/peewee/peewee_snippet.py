# Dommert - PeeWee Notes
# -------------------------------

from flask import Flask
from peewee import *

# flask-peewee bindings
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object(__name__)

# Database 
DATABASE = {
    'name': 'my_database',
    'engine': 'peewee.MySQLDatabase',
    'user': 'db_user',
    'passwd': 'secret password',
    }
DEBUG = True
SECRET_KEY = 'Secret Key!!'

db = Database(app)


# BaseModel Connection
class BaseModel(Model):
    class Meta:
        database = database


# User Class Model
class User(BaseModel)
	username = CharField()
	password = CharField()
	email = CharField()

	Class Meta:
		order_by = ('username',)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
