

import datetime
from beanie import Link
from pydantic import BaseModel

from models.user import User


class Session(BaseModel):
    user_id:Link[User]
    datetime_de_connection: datetime
    
