import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel




class User(BaseModel):
    userID = Optional[str]
    Fname = str
    Lname = str
    phone= str
    created_at = Optional[datetime.date]

    class Config:
        arbitrary_types_allowed = True
    