from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.spartaten

all_users = list(db.users.find({}))

for user in all_users:
    print(user)