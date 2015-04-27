# Flask-PeeWee Example Model

from flask import Flask

# flask-peewee bindings
from flask_peewee.db import Database

# configure our database
DATABASE = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

# instantiate the db wrapper
db = Database(app)

if __name__ == '__main__':
    app.run()