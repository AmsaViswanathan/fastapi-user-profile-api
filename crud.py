from sqlalchemy.orm import Session
from .models import User

def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user: User, name: str):
    user.name = name
    db.commit()
    return user

def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
