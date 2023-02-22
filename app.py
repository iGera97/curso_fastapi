from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Body, Query

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

#Query Validation
@app.post("/person/detail")
def show_detail(
    name : Optional[str] = Query(None,min_length=1,max_length=50,title="Nombre de las persona",description="ingresa tu nombre mi compa"),
    age : int = Query(ge=0)
    ):
    return {name : age}

#Path Parametes Validation
@app.post("/person/detail")
def show_detail(
    name : Optional[str] = Query(None,min_length=1,max_length=50,title="Nombre de las persona",description="ingresa tu nombre mi compa"),
    age : int = Query(ge=0)
    ):
    return {name : age}