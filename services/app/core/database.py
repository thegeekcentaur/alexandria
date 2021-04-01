import pymongo
import os

# Setting up the db and collection for Mongodb.....
MONGO_CONNECTION_URL = os.environ.get('MONGO_CONNECTION_URL', 'mongodb://localhost:27017/')
client = pymongo.MongoClient(MONGO_CONNECTION_URL)
db = client['Book']
collection = db['book']
