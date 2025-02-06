from pymongo.database import Collection

from ..entities.user import User
from ..client import get_collection


class UserRepository:

    def __init__(self, collection: Collection = get_collection('user')):
        self.collection = collection

    def save(self, user: User):
        self.collection.insert_one(user)
