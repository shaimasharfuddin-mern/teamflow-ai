from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        return None

    db_user = User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
):

    db_user = get_user_by_email(db, email)

    if db_user is None:
        return None

    if not verify_password(
        password,
        db_user.hashed_password,
    ):
        return None

    access_token = create_access_token(
        data={
            "sub": db_user.email,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }