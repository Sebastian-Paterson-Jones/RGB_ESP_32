from typing import List, Boolean, Optional
from pydantic import BaseModel


class ColorBase(BaseModel):
    color: str
    title: str


class ColorCreate(ColorBase):
    pass


class ColorUpdate(ColorBase):
    color: Optional[str] = none
    title: Optional[str] = none


class Color(ColorBase):
    id: Int

    class Config:
        orm_mode = True
