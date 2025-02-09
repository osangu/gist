from typing import Annotated, Optional, ClassVar
from pydantic import BaseModel, Field
from pydantic import AliasChoices, PlainSerializer, PlainValidator

from datetime import datetime


class BaseEntity(BaseModel):
    TBL_NAME: ClassVar[str]

    id: Annotated[
        Optional[str],
        PlainValidator(lambda x: str(x)),
        PlainSerializer(lambda x: str(x))
    ] = \
        Field(
            serialization_alias='id',
            validation_alias=AliasChoices('id', '_id'),
        )


class User(BaseEntity):
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
