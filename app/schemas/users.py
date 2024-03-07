from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    ocupation: str
    experience_years: int