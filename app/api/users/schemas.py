from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    """Base user model schema"""
    username: str

    model_config = ConfigDict(
        from_attributes=True
    )
