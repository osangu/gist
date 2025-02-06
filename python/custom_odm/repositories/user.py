from pymongo.database import Collection

from python.custom_odm.entities import User
from python.custom_odm.client import get_collection


class UserRepository:

    def __init__(self, collection: Collection = get_collection('user')):
        self.collection = collection

    def save(self, user: User):
        self.collection.insert_one(user)
