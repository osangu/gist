from datetime import datetime
from typing import Optional

from bson.objectid import ObjectId

from . import fields
from .abc import Entity


class User(Entity, fields.User):
    T_ID = ObjectId

    def __init__(
            self,
            name: str,
            email: str,
            password: str,
            is_approved: bool = False,
            _id: Optional[ObjectId] = None,
            created_at: Optional[datetime] = None,
    ):
        kwargs = {
            self.NAME: name,
            self.EMAIL: email,
            self.PASSWORD: password,
            self.CREATED_AT: created_at,
            self.IS_APPROVED: is_approved,
        }
        if _id is not None:
            kwargs[self.ID] = self._id_T(_id)

        if created_at is None:
            kwargs[self.CREATED_AT] = datetime.now()

        super().__init__(**kwargs)


# if __name__ == '__main__':
#     from ..client import get_collection
#
#     user_col = get_collection('user')
#
#     user = User('osangu', 'hello@gmail.com', 'qwer1234!!')
#
#     res = user_col.insert_one(user)
#     print('res', res)
#
#     find_user = user_col.find_one({User.EMAIL: 'hello@gmail.com'})
#
#     print('find_user', find_user)
#     find_user_entity = User(**find_user)
#
#     print('find_user_entity', find_user_entity)
#
#     print('user_id', find_user_entity.id)
#
#     print('created_at', find_user_entity.created_at)
