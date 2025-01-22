from pydantic import BaseModel, ConfigDict

class Base(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

class UserBase(Base):
    """Base user model schema"""
    username: str


