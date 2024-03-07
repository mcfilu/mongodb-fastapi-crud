from schemas.users import User
from fastapi import HTTPException
from bson.objectid import ObjectId


def create_user_inst(file):
    user_instance = User(first_name=file['first_name'], last_name=file['last_name'], occupancy=file['ocupation'], experience_years=file['experience_years'])
    return user_instance


def get_object_id(user_id):
    try:
        _id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Wrong format of user_id provided")
    return _id