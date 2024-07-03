from datetime import datetime
from beanie import Document, Link

from models.user import User


class Session(Document):
    user_id: Link[User]
    email: str
    name: str
    datetime_de_connection: datetime = datetime.now()
    
