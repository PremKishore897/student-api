from fastapi import FastAPI, status
from models import StudentCreate, StudentUpdate, StudentResponse, CreateStudentResponse, ListStudentsResponse
from database import students_collection
from typing import Union
from bson import ObjectId

def student_helper(student):
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"],
    }

app = FastAPI()
app.title = "Student-API"
app.description = """This API provides endpoints for a Student Management System to manage student records.
There are following endpoints in this API:"""

@app.post("/students", status_code=status.HTTP_201_CREATED, response_model=CreateStudentResponse)
def create_students(student: StudentCreate):
    """API to create a student in the system. All fields are mandatory and required while creating the student in the system."""
    std_instance = students_collection.insert_one(student.model_dump())
    return {"id": str(std_instance.inserted_id)}

@app.get("/students", status_code=status.HTTP_200_OK, response_model=ListStudentsResponse)
def list_students(country: Union[str, None] = None, age: Union[int, None] = None):
    """An API to find a list of students. You can apply filters on this API by passing the query parameters as listed below."""
    query = {}
    if country:
        query["country"] = country
    if age:
        query["age"] = {"$gte": age}
    result = students_collection.find(query).to_list()
    return {"data": [student_helper(student) for student in result]}

@app.get("/students/{id}", status_code=status.HTTP_200_OK, response_model=StudentResponse)
def fetch_student(id: str):
    """An API to find details of a student with id passed in the path."""
    student = students_collection.find_one({"_id": ObjectId(id)})
    return student_helper(student)

@app.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_student(id: str, fields: StudentUpdate):
    """An API to update details of a student with id passed in the path."""
    students_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set":fields.model_dump(exclude_unset=True)})
    return {}

@app.delete("/students/{id}", status_code=status.HTTP_200_OK)
def delete_student(id):
    """An API to delete student record with id passed in the path."""
    students_collection.delete_one({"_id": ObjectId(id)})
    return {}
