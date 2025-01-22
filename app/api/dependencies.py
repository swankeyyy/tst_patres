from fastapi import Header

from .utils import get_username_from_token


def get_credentials_from_header(username: str = Header(None), password: str = Header(None)) -> dict:
    """Take username and password from Header and return dict"""
    return {"username": username, "password": password}


async def get_current_user(token: str = Header(alias="x-token-x")):
    """Get current user from token"""
    username = get_username_from_token(token)
    return username
        