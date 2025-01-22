from fastapi import Header

def get_credentials_from_header(username: str = Header(None), password: str = Header(None)) -> dict:
    """Take username and password from Header and return dict"""
    return {"username": username, "password": password}