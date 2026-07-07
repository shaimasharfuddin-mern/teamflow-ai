from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        print("\n========== JWT DEBUG ==========")
        print("Received Token:", token)
        print("SECRET_KEY:", settings.SECRET_KEY)
        print("ALGORITHM:", settings.ALGORITHM)

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("TOKEN PAYLOAD:", payload)

        user_id = payload.get("user_id")

        if user_id is None:
            print("ERROR: user_id not found in token")
            raise credentials_exception

    except JWTError as e:
        print("JWT ERROR:", str(e))
        raise credentials_exception

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        print("ERROR: User not found in database")
        raise credentials_exception

    print("Authenticated User:", user.email)
    print("===============================\n")

    return user