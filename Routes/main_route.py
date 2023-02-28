from typing import Optional

from pydantic import SecretStr,EmailStr
from fastapi import Cookie, Body, Form, Header, Path, Query, APIRouter, UploadFile, File
from fastapi import status

from Models.location import Location
from Models.login import LoginOut
from Models.person import Person,PersonOut
router = APIRouter()

#Path Operation
@router.get("/",status_code=status.HTTP_200_OK)#Path Operaion decorator
def home():#Path operation function
    return {"Hello" : "World"}

#Request and response body
@router.post("/person/new",response_model=PersonOut,status_code=status.HTTP_201_CREATED)
def create_person(person : Person = Body()):
    return person

#Query Validation
@router.get("/person/detail",status_code=status.HTTP_200_OK)
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
@router.get("/person/detail/{person_id}",status_code=status.HTTP_200_OK)
def show_detail(
    person_id : int = Path(gt=0
                           ,title="id de la persona"
                           ,description="ingresa el id mi compa"
                           ,example=234)
    ):
    return {"id" : person_id}

#Request Body
@router.put("/person/{person_id}",status_code=status.HTTP_200_OK)
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

#Forms
@router.post(path="/login",status_code=status.HTTP_200_OK,response_model=LoginOut)
def login(username : str = Form(max_length=20,min_length=5),
          password : SecretStr = Form(min_length=10,max_length=30)):
    return LoginOut(username=username)

#Cookies and headres parameters
@router.post(path="/contact",status_code=status.HTTP_200_OK)
def contact(first_name : str = Form(max_length=20,min_length=5,example="Pedrito"),
            last_name : str = Form(max_length=20,min_length=5,example="Lopez"),
            email : EmailStr = Form(example="admin@next.com.mx"),
            message : str = Form(min_length=20,example="mi mensaje de prueba es este"),
            user_agent : Optional[str] = Header(default=None),
            ads : Optional[str] = Cookie(default = None)):
    return user_agent

#Files
@router.post(path="/post-image")
def post_image(image : UploadFile = File()):
    print(image.content_type)
    return {
        "Filename" : image.filename,
        "Format" : image.content_type,
        "Size(kb)": len(image.file.read())
    }