from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import sys
import os

print(sys.argv)
load_dotenv("secrets.env")

URI = os.getenv("DATABASE_URI")
# print(URI)
# Create a new client and connect to the server
client = MongoClient(URI)
db = client.get_database("studentsDB")
students_collection = db.get_collection("students")