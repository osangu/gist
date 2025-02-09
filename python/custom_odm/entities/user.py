import enum
from datetime import datetime, timedelta, timezone

from pydantic import Field

from . import abc


def kst_now() -> datetime:
    tz = timezone(timedelta(hours=9))

    return datetime.now(tz=tz)


class U_Role(str, enum.Enum):
    USER = 'user'
    ADMIN = ''


class User(abc.User):
    TBL_NAME = 'User'

    name: str
    email: str
    password: str
    is_approved: bool = Field(default=False)
    role: U_Role = Field(default=U_Role.USER)
    created_at: datetime = Field(default_factory=kst_now)
