from fastapi import APIRouter


router = APIRouter()


@router.get("/users/{user_id}")
def get_user_by_id(user_id:int):
    pass


@router.delete("/users/{user_id}")
def delete_user_by_id(user_id:int):
    pass


@router.post("/users/new")
def create_new_user():
    pass


@router.put("/users/{user_id}")
def update_user_by_id(user_id:int):
    pass