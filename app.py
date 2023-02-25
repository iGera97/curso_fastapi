from typing import Optional
from enum import Enum
from pydantic import BaseModel,Field,SecretStr
from fastapi import FastAPI, Body, Path, Query

app = FastAPI()

#Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blond = "blond"

class PersonBase(BaseModel):
    first_name : str = Field(min_length=1,max_length=50,example="Paquito")
    last_name : str = Field(min_length=1,max_length=50,example="Perez")
    age : int = Field(gt=0,le=115,example=12)
    hair_color : Optional[HairColor] = Field(None,example="brown")
    is_married : Optional[bool] = Field(None,example=True)
    """class Config:
        schema_extra = {
            "example" : {
                "first_name" : "Fulano",
                "last_name" : "Pérez",
                "age" : "40",
                "hair_color" : "black",
                "is_married" : True,
                "password" : "84bbfu4bdsjkd"
            }
        }"""

class Person(PersonBase):
    password : SecretStr = Field(min_length=10,max_length=30,example="84bbfu4bdsjkd")

class PersonOut(PersonBase):
    pass

class Location(BaseModel):
    city : str
    state : str
    country : str

    class Config:
        schema_extra = {
            "example": {
                "city": "Oaxaca de Juarez",
                "state": "Oaxaca",
                "country": "Mexico",
        }
        }

#Path Operation
@app.get("/")#Path Operaion decorator
def home():#Path operation function
    return {"Hello" : "World"}

#Request and response body
@app.post("/person/new",response_model=PersonOut)
def create_person(person : Person = Body()):
    return person

#Query Validation
@app.get("/person/detail")
def show_detail(
    name : Optional[str] = Query(None,
                                min_length=1,
                                max_length=50,
                                title="Nombre de las persona",
                                description="ingresa tu nombre mi compa",
                                example="Pedrito"),
    age : int = Query(ge=0,example=50)
    ):
    return {name : age}

#Path Validation
@app.get("/person/detail/{person_id}")
def show_detail(
    person_id : int = Path(gt=0
                           ,title="id de la persona"
                           ,description="ingresa el id mi compa"
                           ,example=234)
    ):
    return {"id" : person_id}

#Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id : int = Path(gt=0,
                            title="id de la persona",
                            description="ingresa el id mi compa",
                            example=22),
    person : Person = Body(),
    location : Location = Body()
    ):

    result = person.dict()
    result.update(location.dict())

    return result