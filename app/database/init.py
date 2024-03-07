from pytube import MongoClient

conn_string = "mongodb://localhost:27017/"

client = MongoClient()
users_db = client.data
users_collections = users_db.users