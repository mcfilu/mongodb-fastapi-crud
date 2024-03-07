from fastapi import FastAPI
import os
import pprint
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
conn_string = "mongodb://localhost:27017/data"

print(os.environ.get("MONGODB_PWD"))
client = MongoClient(conn_string)
dbs = client.list_database_names()
data_db = client.data
collections = data_db.list_collection_names()
user_collection = data_db.users

print(dbs)
print(data_db)
print(collections)

printer = pprint.PrettyPrinter()

def insert_user():
    new_user = {
        "first_name": "Mathew",
        "last_name": "Gunner",
        "ocupation": "Driver", 
        "experience_years": 8,
    }
    id = user_collection.insert_one(new_user).inserted_id
    print(id)

# insert_user()

def get_all():
    all_users = user_collection.find_one({"experience_years": 4})
    print(all_users)
    # list_users = list(all_users)
    # print(list_users)
    # print(list_users[0])
    # print('asdfas')
    for user in all_users:
        printer.pprint(user)

get_all()

def get_one():
    pass


app = FastAPI()



