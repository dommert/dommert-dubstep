# Dommert Enterprises
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