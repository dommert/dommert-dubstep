db = SqliteDatabase('custom.db')

class RumModel(Model):
    class Meta:
        database = db

class User(CustomModel):
    username = CharField()

db.connect()
RumModel.create_table()
