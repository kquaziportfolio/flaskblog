import pymongo
import os


class Database:
    DB = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(os.environ['MONGOLAB_URI'])
        Database.DB = client.mydb

    @staticmethod
    def insert_record(doc):
        Database.DB.entries.insert(doc)

    @staticmethod
    def get_records():
        return [x for x in Database.DB.entries.find({})]

    @staticmethod
    def delete_records():
        Database.DB.entries.remove({})

    @staticmethod
    def delete_doc(key, value):
        Database.DB.entries.drop({key, value})

    @staticmethod
    def edit_doc(sieve, new_doc):
        Database.DB.entries.update_one(sieve, {"$set": new_doc})
