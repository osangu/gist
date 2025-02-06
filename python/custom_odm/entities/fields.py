from datetime import datetime


class User:
    name: str
    email: str
    password: str
    is_approved: bool
    created_at: datetime

    NAME = 'name'
    EMAIL = 'email'
    PASSWORD = 'password'
    CREATED_AT = 'created_at'
    IS_APPROVED = 'is_approved'
