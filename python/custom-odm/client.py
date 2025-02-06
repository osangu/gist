from typing import List

from pymongo import MongoClient
from pymongo.database import Database, Collection
from pymongo.errors import CollectionInvalid

from .config import DatabaseConfig

client = MongoClient(DatabaseConfig.URL)

db = client.get_database(DatabaseConfig.NAME)


def init_mongo():
    create_collections([])
    create_indexes()


def create_collections(names: List[str]):
    for name in names:
        try:
            db.create_collection(name)

        except CollectionInvalid:
            """
            Do Something In here
            """
            pass

def create_indexes():
    pass


def get_collection(name: str) -> Collection:
    return db.get_collection(name)
