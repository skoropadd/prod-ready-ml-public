"""FastAPI example demonstrating Pydantic input/output validation and filtering."""

from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseUser(BaseModel):
    """Fields common to all user representations."""

    id: int
    name: str = "John Doe"
    friend_ids: list[int] | None = None


class User(BaseUser):
    """Full user — includes sensitive fields. Used for input."""

    signup_ts: datetime | None = None
    password: str


class SafeUser(BaseUser):
    """User without sensitive fields. Used for safe output."""

    pass  # only the base fields


@app.post("/user")
async def read_user(user: User) -> User:
    """Echo the user back, full data."""
    return user


@app.post("/safe_user")
async def read_safe_user(user: User) -> SafeUser:
    """Accept a full User, return SafeUser (password and signup_ts stripped)."""
    return user
