from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    name: str
    fee:int 


class Event(BaseModel):
    event_id: str
    event_name: str
    price: int
    max_participants: Optional[int] = None
