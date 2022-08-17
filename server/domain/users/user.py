from pydantic import BaseModel

class CreateUser(BaseModel):
    name:str
    username:str
    password:str


class User(CreateUser):
    id: str = None
    password: str = None
