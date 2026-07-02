from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import User
from app.schemas.user import UserCreate

ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


# ----------------------------------------
# PASSWORD UTILITIES
# ----------------------------------------

def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
):
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


# ----------------------------------------
# CREATE USER
# ----------------------------------------

def create_user(
    db: Session,
    user: UserCreate,
):
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

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


# ----------------------------------------
# CREATE JWT TOKEN
# ----------------------------------------

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
):
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=60)
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )


# ----------------------------------------
# LOGIN
# ----------------------------------------

def authenticate_user(
    db: Session,
    email: str,
    password: str,
):
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.hashed_password,
    ):
        return None

    access_token = create_access_token(
        data={
            "sub": user.email,
            "user_id": user.id,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }