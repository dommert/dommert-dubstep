psql_db = PostgresqlDatabase('my_database', user='code')
# if your Postgres template doesn't use UTF8, you can set the connection encoding like so:
psql_db.get_conn().set_client_encoding('UTF8')


class PostgresqlModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class User(PostgresqlModel):
    username = CharField()