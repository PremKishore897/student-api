from pymongo.mongo_client import MongoClient
import os

URI = os.getenv("DATABASE_URI")
# print(URI)
# Create a new client and connect to the server
client = MongoClient(URI)
db = client.get_database("studentsDB")
students_collection = db.get_collection("students")
