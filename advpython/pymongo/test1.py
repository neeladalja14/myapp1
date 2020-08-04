import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]

users = mydb.users

user1 = [{"username": "third", "password": "1234"}, {"username": "red", "password": "blue"}, {"username": "hola", "password": "helo"}]

Users = mydb.users
exit

inserted = Users.insert_many(users)

inserted.inserted_ids

