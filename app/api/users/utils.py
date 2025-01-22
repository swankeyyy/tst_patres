from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.src.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Takes password and return hashed password"""
    return pwd_context.hash(password)


def password_verify(password: str, username: str) -> bool:
    """Verify password against username"""
    if password != username and len(password) > 4:
        return True
    return False


def check_password(password: str, user_password: str) -> str:
    """Check password against hashed password"""
    return pwd_context.verify(password, user_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create access token with data and expiration time"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.TOKEN_SECRET_KEY, algorithm=settings.HASH_ALGORITHM
    )
    return encoded_jwt
