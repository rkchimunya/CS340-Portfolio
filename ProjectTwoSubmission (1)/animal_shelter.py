# Example Python Code to Insert a Document 
from urllib.parse import quote_plus
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. 
        USER = quote_plus(username)
        PASS = quote_plus(password)
        HOST = '127.0.0.1'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                # Use insert_one for industry standard practice
                insert_result = self.collection.insert_one(data) 
                return insert_result.acknowledged
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R in CRUD
    def read(self, searchData):
        try:
            if searchData:
                # find() returns a cursor, which we convert to a list
                data = self.collection.find(searchData, {"_id": False})
            else:
                data = self.collection.find({}, {"_id": False})
            return list(data)
        except Exception as e:
            print(f"An error occurred during read: {e}")
            return []

    # Update and Delete are for Project One, but keeping your placeholders 
    # aligned here so they don't cause errors now.
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.collection.update_many(searchData, {"$set": updateData})
            return result.raw_result
        return "{}"

    def delete(self, deleteData):
        if deleteData is not None:
            result = self.collection.delete_many(deleteData)
            return result.raw_result
        return "{}"