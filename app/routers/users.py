from fastapi import APIRouter
from crud.users import get_one_user
from schemas.users import User
import pprint

printer = pprint.PrettyPrinter()

router = APIRouter()


@router.get("/users/{user_id}")
def get_user_by_id(user_id:str):
    user_data = get_one_user(user_id)
    pprint.pprint(user_data)
    return user_data




@router.delete("/users/{user_id}")
def delete_user_by_id(user_id:int):
    pass


@router.post("/users/new")
def create_new_user(user_obj: User):
    pass


@router.put("/users/{user_id}")
def update_user_by_id(user_id:int, user_obj: User):
    pass