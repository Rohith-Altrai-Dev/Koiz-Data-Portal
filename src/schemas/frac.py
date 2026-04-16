from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class AccessType(str, Enum):
    ENTER = "enter"
    EXIT = "exit"

class AccessEvent(BaseModel):
    occupant_id: str
    building_id: str
    event: AccessType
    timestamp: datetime