# Dommert Enterprises
# PeeWee MySQL Connection

from flask import Flask
from peewee import *

# flask-peewee bindings
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object(__name__)



mysql = MySQLDatabase('my_database', user='code')


class MySQLModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql

class User(MySQLModel):
    username = CharField()
    # etc, etc


# when you're ready to start querying, remember to connect
mysql.connect()