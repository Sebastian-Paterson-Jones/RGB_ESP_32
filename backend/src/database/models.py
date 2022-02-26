from sqlalchemy import Column, Integer, String
from db import Base


class Color(Base):
    __tablename__ = "color_list"
    id = Column(Integer, primary_key=True, index=True)
    color: Column(String)
    title: Column(String)
