# Database Wrappers

# Flask-PeeWee
from flask import Flask
from peewee import *

from flask_peewee.db import Database


# SQLite
DATABASE = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
}


# MySQL
DATABASE = {
    'name': 'my_database',
    'engine': 'peewee.MySQLDatabase',
    'user': 'db_user',
    'passwd': 'secret password',
}

# Prostrege
DATABASE = {
    'name': 'my_db',
    'engine': 'peewee.PostgresqlDatabase',
    'user': 'postgres',
    'threadlocals': True, # <-- this
}


# 
app = Flask(__name__)
app.config.from_object(__name__) # load database configuration from this module

# instantiate the db wrapper
db = Database(app)

# start creating models
class Blog(db.Model):
    name = CharField()
    # .. etc