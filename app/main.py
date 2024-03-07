from fastapi import FastAPI
import os
import pprint
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from bson.objectid import ObjectId
from pydantic import BaseModel

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

# get_all()

def get_one(user_id):
    _id = ObjectId(user_id)
    user = user_collection.find_one({"_id":_id})
    printer.pprint(user)


# get_one("65e90d331f0c26e56a602b13")



def get_some_cols():
    cols = {"_id": 0, "first_name": 1, "last_name": 1}
    users = user_collection.find({}, cols)
    for user in users:
        printer.pprint(user)

# get_some_cols()
        
def query_users_by_exp(start, end):
    query = {
        "$and": [
            {"experience_years": {"$gte": start}}, 
            {"experience_years": {"$lte": end}}
        ]
    }
    result = user_collection.find(query).sort("experience_years", -1)

    for user in result:
        printer.pprint(user)

query_users_by_exp(2,8)

def delete_by_id(user_id):
    _id = ObjectId(user_id)
    deleted = user_collection.delete_one({"_id": _id})
    print(deleted.deleted_count)

# delete_by_id("65e90b4cadc232407580175a")
    

class User(BaseModel):
    first_name: str
    last_name: str
    occupancy: str
    experience_years: int


def update_user_by_id(user_id, data):
    _id = ObjectId(user_id)
    updated = user_collection.update_one({"_id": _id}, {"$set": {"first_name": data.first_name, "last_name": data.last_name, "occupancy": data.occupancy, "experience_years": data.experience_years}})
    print(updated.modified_count)

new_user = User(first_name="Lazio", last_name="Olsu", occupancy="Softweare", experience_years=5)

# update_user_by_id("65e90d331f0c26e56a602b13", new_user)

app = FastAPI()



