# Dommert - PeeWee Notes

# Database Connection
database = type(DATABASE_)

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
