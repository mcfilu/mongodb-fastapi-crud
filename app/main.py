from fastapi import FastAPI
import os
import pprint
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
conn_string = "mongodb://localhost:27017/data"

print(os.environ.get("MONGODB_PWD"))
client = MongoClient(conn_string)
print(client)


app = FastAPI()



