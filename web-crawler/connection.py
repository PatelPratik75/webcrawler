from pymongo import MongoClient
# uri
uri = 'localhost:27017'
client = MongoClient(uri)
db = client.Health
