


from beanie import Document, Link

from models.user import User


class Session(Document):
    user_id:Link[User]
    datetime_de_connection: str
    
