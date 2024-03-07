from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    occupancy: str
    experience_years: int