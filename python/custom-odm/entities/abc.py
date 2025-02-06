from uuid import UUID

from typing import Union, Type
from bson.objectid import ObjectId


class Entity(dict):
    ID = '_id'
    T_ID: Type[Union[ObjectId, UUID]]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def id(self) -> str:
        entity_id = self.get(self.ID)

        return str(entity_id)

    @id.setter
    def id(self, value):
        entity_id = Entity.T_ID(value)

        self[self._id] = entity_id

    def __getattr__(self, item):
        """
        value = getattr(self, item.upper())

        Upper script can make circular usage
        """
        value = self.__getattribute__(item.upper())

        return self.get(value)


__all__ = ["Entity"]
