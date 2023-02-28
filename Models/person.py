from typing import Optional
from pydantic import BaseModel,Field,SecretStr
from Models.hair_color import HairColor

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