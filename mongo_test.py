import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

db = client['user_name']
mycol = db['col']

mydict = {'name': 'John', 'age': '37'}

x = mycol.insert_one(mydict)
