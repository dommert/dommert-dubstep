# Dommert Enterprises
# MySQL Connection

mysql_db = MySQLDatabase('my_database', user='code')


class MySQLModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db

class User(MySQLModel):
    username = CharField()
    # etc, etc


# when you're ready to start querying, remember to connect
mysql_db.connect()