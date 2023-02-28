from typing import Optional

from fastapi import (APIRouter, Body, Cookie, File, Form, Header,
                     HTTPException, Path, Query, UploadFile, status)
from pydantic import EmailStr, SecretStr

from Models.location import Location
from Models.login import LoginOut
from Models.person import Person, PersonOut

router = APIRouter()

#Path Operation
@router.get("/",status_code=status.HTTP_200_OK)#Path Operaion decorator
def home():#Path operation function
    '''
    Ruta principal de la API

    Returns:
        dict: Un diccionario con el mensaje de bienvenida
    '''
    return {"Hello" : "World"}

#Request and response body
@router.post("/person/new",response_model=PersonOut,status_code=status.HTTP_201_CREATED,tags=["Persons"],summary="Create Person in teh app")
def create_person(person : Person = Body()):
    '''
        # Create Person

        Función para crear una nueva persona en la aplicación.

        Parametros:
        - request body parameter:
            - **person: Person** -> Modelo de persona con los campos first_name,last_name,age,haor_color, is_married y password

        Regresa un modelo de persona con los campos first_name,last_name,age,hair_color y  is_married
    '''
    return person

#Query Validation
@router.get("/person/detail",status_code=status.HTTP_200_OK,tags=["Persons"])
def show_detail(
    name : Optional[str] = Query(None,
                                min_length=1,
                                max_length=50,
                                title="Nombre de las persona",
                                description="ingresa tu nombre mi compa",
                                example="Pedrito"),
    age : int = Query(ge=0,example=50)
    ):
    """
    Muestra detalles de una persona específica

    Args:
        name (Optional[str], optional): Nombre de la persona a buscar. Defaults to None.
        age (int, optional): Edad de la persona a buscar. Defaults to Query(ge=0, example=50).

    Returns:
        dict: Un diccionario con el nombre y la edad de la persona
    """
    return {name : age}

#Path Validation
@router.get("/person/detail/{person_id}",status_code=status.HTTP_200_OK,tags=["Persons"])
def show_detail(
    person_id : int = Path(gt=0
                           ,title="id de la persona"
                           ,description="ingresa el id mi compa"
                           ,example=234)
    ):
    """
    Muestra detalles de una persona específica

    Args:
        person_id (int): ID de la persona a buscar

    Raises:
        HTTPException: Si no se encuentra una persona con el ID especificado

    Returns:
        dict: Un diccionario con el ID de la persona
    """
    persons = [1,2,3,4,5]
    if person_id not in persons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No se encuentra una persona con el id {person_id}")
    return {"id" : person_id}

#Request Body
@router.put("/person/{person_id}",status_code=status.HTTP_200_OK,tags=["Persons"])
def update_person(
    person_id : int = Path(gt=0,
                            title="id de la persona",
                            description="ingresa el id mi compa",
                            example=22),
    person : Person = Body(),
    location : Location = Body()
    ):
    """
    Actualiza una persona en la aplicación

    Args:
        person_id (int): ID de la persona a actualizar
        person (Person): Modelo de persona con los campos a actualizar
        location (Location): Modelo de ubicación con los campos a actualizar

    Returns:
        dict: Un diccionario con los campos actualizados de la persona y la ubicación
    """

    result = person.dict()
    result.update(location.dict())

    return result

#Forms
@router.post(path="/login",status_code=status.HTTP_200_OK,response_model=LoginOut,tags=["Persons"])
def login(username : str = Form(max_length=20,min_length=5),
          password : SecretStr = Form(min_length=10,max_length=30)):
    return LoginOut(username=username)

#Cookies and headres parameters
@router.post(path="/contact",status_code=status.HTTP_200_OK,tags=["Cookies"])
def contact(first_name : str = Form(max_length=20,min_length=5,example="Pedrito"),
            last_name : str = Form(max_length=20,min_length=5,example="Lopez"),
            email : EmailStr = Form(example="admin@next.com.mx"),
            message : str = Form(min_length=20,example="mi mensaje de prueba es este"),
            user_agent : Optional[str] = Header(default=None),
            ads : Optional[str] = Cookie(default = None)):
    return user_agent

#Files
@router.post(path="/post-image",tags=["Images"])
def post_image(image : UploadFile = File()):
    print(image.content_type)
    return {
        "Filename" : image.filename,
        "Format" : image.content_type,
        "Size(kb)": len(image.file.read())
    }