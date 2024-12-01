from pydantic import BaseModel
from typing import Optional, List

class Address(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    address: Address

class CreateStudentResponse(BaseModel):
    id: str

class ListStudentsResponse(BaseModel):
    data: List[StudentResponse]