from pydantic import BaseModel, PlainSerializer, ConfigDict

uuid_to_str: Callable[[UUID], str] = (lambda x: str(x))

class Bar(BaseModel):
    b: Annotated[UUID, PlainSerializer(uuid_to_str)]
    ar: Annotated[UUID, PlainSerializer(uuid_to_str)]

    ba: str
    r: datetime


class FooBar(BaseModel):
    foo: Annotated[UUID, PlainSerializer(uuid_to_str)]
    bar: Annotated[UUID, PlainSerializer(uuid_to_str)]

    __pydantic_extra__: Dict[
        Annotated[Union[str, UUID], PlainSerializer(uuid_to_str)],
        Bar
    ]

    model_config = ConfigDict(extra='allow')
