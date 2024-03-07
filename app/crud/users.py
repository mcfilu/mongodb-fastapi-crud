import pprint
from database.init import users_collections
from schemas.users import User
from fastapi import HTTPException
from helpers.make_users import get_object_id, create_user_inst
from bson.objectid import ObjectId

printer = pprint.PrettyPrinter()

def insert_user(user_obj):
    try:
        id = str(users_collections.insert_one(dict(user_obj)).inserted_id)
    except Exception:
        raise HTTPException(status_code=404, detail="There was a problem inserting a new document")
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
    users_list = []
    query = {
        "$and": [
            {"experience_years": {"$gte": start}}, 
            {"experience_years": {"$lte": end}}
        ]
    }
    result = users_collections.find(query).sort("experience_years", -1)

    for user in result:
        users_list.append(create_user_inst(user))

    return users_list



def delete_by_id(user_id):
    _id = get_object_id(user_id)
    deleted = users_collections.delete_one({"_id": _id}).deleted_count
    if deleted == 0:
        raise HTTPException(status_code=404, detail="No object was deleted, it couldnt be found")
    return deleted



def update_user_by_id_crud(user_id, data):
    _id = get_object_id(user_id)
    updated_count = users_collections.update_one({"_id": _id}, {"$set": {"first_name": data.first_name, "last_name": data.last_name, "ocupation": data.ocupation, "experience_years": data.experience_years}}).modified_count
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="No user file found with such id")
    return updated_count


