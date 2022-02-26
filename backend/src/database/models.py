from typing import List
from pydantic import BaseModel

class Color(BaseModel):
    color: str
    title: str

class ColorList(BaseModel):
    data: List[Color]