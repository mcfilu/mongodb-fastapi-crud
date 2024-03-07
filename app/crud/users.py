import pprint
from database.init import users_collections
from schemas.users import User
from fastapi import HTTPException
from helpers.make_users import get_object_id
from bson.objectid import ObjectId

printer = pprint.PrettyPrinter()

def insert_user(user_obj):
    id = str(users_collections.insert_one(dict(user_obj)).inserted_id)
    printer.pprint(id)
    return id


def get_all():
    all_users = users_collections.find_one({"experience_years": 4})
    print(all_users)
    for user in all_users:
        printer.pprint(user)


def get_one_user(user_id):
    _id = get_object_id(user_id)
    one_user = users_collections.find_one({"_id":_id})
    if not one_user:
        raise HTTPException(status_code=404, detail="Such user does not exist")
    return one_user


def get_some_cols():
    cols = {"_id": 0, "first_name": 1, "last_name": 1}
    users = users_collections.find({}, cols)
    for user in users:
        printer.pprint(user)


        
def query_users_by_exp(start, end):
    query = {
        "$and": [
            {"experience_years": {"$gte": start}}, 
            {"experience_years": {"$lte": end}}
        ]
    }
    result = users_collections.find(query).sort("experience_years", -1)

    for user in result:
        printer.pprint(user)



def delete_by_id(user_id):
    _id = get_object_id(user_id)
    deleted = users_collections.delete_one({"_id": _id}).deleted_count
    if deleted == 0:
        raise HTTPException(status_code=404, detail="No object was deleted, it couldnt be found")
    return deleted



def update_user_by_id(user_id, data):
    _id = ObjectId(user_id)
    updated = users_collections.update_one({"_id": _id}, {"$set": {"first_name": data.first_name, "last_name": data.last_name, "occupancy": data.occupancy, "experience_years": data.experience_years}})
    print(updated.modified_count)


