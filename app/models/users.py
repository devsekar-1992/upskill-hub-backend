from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


# Base Model without table [Used for pydantic validation]
class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str


# Model for user creation [Extends UserBase, adds password]
class UserCreate(UserBase):
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


# Model for API Response [Includes ID & Timestamps, excludes password]
class UserResponse(UserBase):
    id: int
    email: str


# SQLModel table for database storage
class Users(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
