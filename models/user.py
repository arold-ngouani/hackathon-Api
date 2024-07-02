
from beanie import Document, Indexed


class User(Document):
    name:str 
    email: Indexed(str, unique=True)
    role:str
        