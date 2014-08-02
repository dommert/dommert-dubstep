# An interesting pattern is also to use classes and inheritance for configuration:

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

# To enable such a config you just have to call into from_object():
#app.config.from_object('configmodule.ProductionConfig')

