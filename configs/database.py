import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
class MongoDB:
    def __init__(self, uri: str = os.getenv("MONGODB_URL"), db_name: str = os.getenv("MONGODB_DATABASE")):
        self.client = MongoClient(uri)
        self.database = self.client[db_name]

    def get_collection(self, collection_name: str):
        return self.database[collection_name]

db_instance = MongoDB()