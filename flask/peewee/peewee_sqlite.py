# Dommert Enterprises
# Flask-PeeWee SQLite
from flask import Flask
from peewee import *

# flask-peewee bindings
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object(__name__)

sqlite_db = SqliteDatabase('sq.db')


class SqliteModel(Model):
    """A base model that will use our Sqlite database"""
    class Meta:
        database = sqlite_db

class User(SqliteModel):
    username = CharField()
    # etc, etc


# when you're ready to start querying, remember to connect
sqlite_db.connect()