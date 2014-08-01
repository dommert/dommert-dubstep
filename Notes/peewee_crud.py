#PeeWee CRUD
# ======================

# TABLE: Model.create_table()
# CREATE: model.create()
# 	model.save()
# READ: model.get()  model.select()
# UPDATE: model.insert()
# DELETE:  model.delete_instance()
#

# COUNTING: model.select().count()
# SELECT: model.select().where(model.id = 1)
# AGGREGATING: model.select(user.id = 1).annotate(tweet)



# --------- Starting Point

from PeeWee import *

contacts_db = SqliteDatabase('contacts.db')




# ------  CREATE

#style 1

model.create(user='Monkey')

#Style 2 
model = model()
model.user = 'Monkey'
user.save()
user.id


# -------  INSERT

model.insert(user='admin', active=True, registration_expired=False)
# 
model.get(model.user=='sex_machine')
echo model.save()

# -- Traversing foriegn keys 
  # objects: tweet & user
tweet.user.username


