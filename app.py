from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Body

app = FastAPI()

#Models
class Person(BaseModel):
    first_name : str
    last_name : str
    age : int
    hair_color : Optional[str] = None
    is_married : Optional[bool] = None

#Path Operation
@app.get("/")#Path Operaion decorator
def home():#Path operation function
    return {"Hello" : "World"}

#Request and response body
@app.post("/person/new")
def create_person(person : Person = Body()):
    return person