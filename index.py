from fastapi import FastAPI, Body, Depends
from sqlalchemy.orm import joinedload
from model import Base, University

from database import Session, engine

app = FastAPI()
# Creating_table()

Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


# 1 Get post for testing
@app.get("/api", tags=["Testing"])
def hello_world():
    return {"message": "Hello World"}


@app.get("/university")
def get_university(db: Session = Depends(get_db)):
    university = db.query(University).all()
    return university
