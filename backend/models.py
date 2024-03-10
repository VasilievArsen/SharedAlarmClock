from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

class Alarm(BaseModel):
    id: int
    name: str
    time: str
    owner_id: int
    participants: list
