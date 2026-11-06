from fastapi import Depends, FastAPI,HTTPException,status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base, UserDB
from app.schemas import UserCreate, UserRead

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/api/requests", response_model=UserRead, status_code=status.HTTP_201_CREATED,)
def add_user(new_user:UserCreate, db:Session=Depends(get_db)):
    db_user=UserDB(**new_user.model_dump())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This user already exists",)
    return db_user
@app.get("/api/requests",response_model=list[UserRead])
def get_users(db:Session=Depends(get_db)):
    statement = select(UserDB).order_by(UserDB.id)
    return db.execute(statement).scalars().all()


