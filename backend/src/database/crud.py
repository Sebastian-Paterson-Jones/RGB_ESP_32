from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def get_colors(db: Session):
    return db.query(models.Color)


def get_color(db: Session, color_id: int):
    db_color = db.query(models.Color).filter(models.Color.id == color_id).first()
    if not db_color:
        raise HTTPException(status_code=404, detail="Color not found")
    return db_color


def update_color(db: Session, color_id: int, color: schemas.ColorUpdate):
    db_color = db.query(models.Color).filter(models.Color.id == color_id).first()
    if not db_color:
        raise HTTPException(status_code=404, detail="Color not found")
    color_data = color.dict(exclude_unset=True)
    for key, value in color_data.items():
        setattr(db_color, key, value)
    session.add(db_color)
    session.commit()
    session.refresh(db_color)
    return db_color
