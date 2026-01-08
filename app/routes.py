from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud, schemas, external_api

router = APIRouter()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST - Create user using External API
@router.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(db: Session = Depends(get_db)):
    # Fetch user from external API
    external_user = external_api.get_random_user()

    # Save to database
    return crud.create_user(
        db,
        name=external_user["name"],
        email=external_user["email"]
    )

# GET - Get user by ID
@router.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# PUT - Update user name
@router.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.update_user(db, user, user_update.name)

# DELETE - Delete user
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    crud.delete_user(db, user)
    return {"message": "User deleted successfully"}
