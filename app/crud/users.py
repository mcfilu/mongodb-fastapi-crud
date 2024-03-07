import pprint
from database.init import users_collections
from schemas.users import User
from bson.objectid import ObjectId

printer = pprint.PrettyPrinter()

def insert_user():
    new_user = {
        "first_name": "Mathew",
        "last_name": "Gunner",
        "ocupation": "Driver", 
        "experience_years": 8,
    }
    id = users_collections.insert_one(new_user).inserted_id
    print(id)


def get_all():
    all_users = users_collections.find_one({"experience_years": 4})
    print(all_users)
    for user in all_users:
        printer.pprint(user)


def get_one(user_id):
    _id = ObjectId(user_id)
    user = users_collections.find_one({"_id":_id})
    printer.pprint(user)






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
    _id = ObjectId(user_id)
    deleted = users_collections.delete_one({"_id": _id})
    print(deleted.deleted_count)    



def update_user_by_id(user_id, data):
    _id = ObjectId(user_id)
    updated = users_collections.update_one({"_id": _id}, {"$set": {"first_name": data.first_name, "last_name": data.last_name, "occupancy": data.occupancy, "experience_years": data.experience_years}})
    print(updated.modified_count)


