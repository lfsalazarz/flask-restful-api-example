from typing import List
from datetime import datetime
from pydantic import BaseModel


class ItemSchema(BaseModel):
    name: str
    serial: int
    date: datetime = None
    colors: List[str] = []
