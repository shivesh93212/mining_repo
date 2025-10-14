import os

client = None
db = None
_use_pymongo = False

def connect_db():
    global client, db, _use_pymongo
    try:
        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27017/")
        db = client["smart_energy_mine"]
        _use_pymongo = True
        print("✅ Connected to MongoDB")
    except Exception as e:
        # Fallback to an in-memory dictionary to allow the app to run in environments without MongoDB
        print("Warning: pymongo not available or MongoDB not reachable — using in-memory fallback. Details:", e)
        client = None
        db = InMemoryDB()

class InMemoryCollection:
    def __init__(self):
        self._data = []
    def insert_one(self, doc):
        self._data.append(dict(doc))
    def find(self, *args, **kwargs):
        for d in self._data:
            yield d

class InMemoryDB:
    def __init__(self):
        self.energy_readings = InMemoryCollection()

def get_db():
    return db
