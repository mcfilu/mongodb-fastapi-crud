from fastapi import APIRouter, HTTPException
from crud.users import get_one_user, delete_by_id, insert_user
from helpers.make_users import create_user_inst
from schemas.users import User
import pprint

printer = pprint.PrettyPrinter()

router = APIRouter()


@router.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id:str):
    """
    Get User By Id endpoint

    Requries the _id field from the mongodb passed as a string

    Returns the User object with the following attributes: first_name, last_name, occupancy, experience_years
    """
    user_data = get_one_user(user_id)
    user_instance = create_user_inst(user_data)
    return user_instance




@router.delete("/users/{user_id}")
def delete_user_by_id(user_id:str):
    """
    Delete Use By ID endpoint

    Required the _id field from the mongodb passed as a string

    Returns an akcknlowedgment when user file is deleted from db or raises an error if happens
    """
    result = delete_by_id(user_id)

    if result == 1:
        return {"acknowledgmenet": True}
    
    else:
        raise HTTPException(status_code=404, detail="Some Error occured")
    


@router.post("/users/new")
def create_new_user(user_obj: User):
    """
    Create New User endpoint

    Required the User object with field: first_name, last_name, occupancy, experience_years

    Return and id of newly created object
    """
    new_id = insert_user(user_obj)
    printer.pprint(new_id)
    return {"message": "User created", "id": new_id}


@router.put("/users/{user_id}")
def update_user_by_id(user_id:int, user_obj: User):
    pass