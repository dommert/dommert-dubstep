# Flask-PeeWee
# API Exclude

from flask_peewee.rest import RestAPI, RestResource

from app import app # our project's Flask app

# instantiate our api wrapper
api = RestAPI(app)

# create a special resource for users that excludes email and password
class UserResource(RestResource):
    exclude = ('password', 'email',)

# register our models so they are exposed via /api/<model>/
api.register(User, UserResource) # specify the UserResource
api.register(Relationship)
api.register(Message)