from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#Path Operation
@app.get("/")#Path Operaion decorator
def home():#Path operation function
    return {"Hello" : "World"}

#Path Parameter
@app.get("/ids/{id_}")
def get_id(id_ : int):
    return {
        "Id" : id_
    }

#Query Parameter
@app.get("/ids/{id_}/details")
def get_id(id_ : int,age : Optional[int] = None):
    
    return {
        "Id" : id_,
        "age" : age
    }