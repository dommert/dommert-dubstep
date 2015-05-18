#Example of inserting multiple Users:

usernames = ['charlie', 'huey', 'peewee', 'mickey']
row_dicts = ({'username': username} for username in usernames)

# Insert 4 new rows.
User.insert_many(row_dicts).execute()

#Because the rows parameter can be an arbitrary iterable, you can also use a generator:

def get_usernames():
    for username in ['charlie', 'huey', 'peewee']:
        yield {'username': username}
User.insert_many(get_usernames()).execute()

