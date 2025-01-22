from passlib.context import CryptContext

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
