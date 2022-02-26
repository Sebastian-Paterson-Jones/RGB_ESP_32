from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db  = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# route to get colors
@app.get("/colors", response_model=List[schemas.Color])
def get_colors(db: Session = Depends(get_db())):
    return crud.get_colors(db)


# route to get color
@app.get("/colors/{color_id}", response_model=schemas.Color)
def get_color(color_id: int, db: Session = Depends(get_db())):
    return crud.get_color(db, color_id)


# route to patch colours
@app.patch("/colors/{color_id}", response=schemas.Color)
def update_color(color_id: int, color: schemas.ColorUpdate, db: Session = Depends(get_db())):
    return crud.update_color(db, color_id, color)

