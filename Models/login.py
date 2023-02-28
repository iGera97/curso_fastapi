from pydantic import BaseModel,Field

class LoginOut(BaseModel):
    username : str = Field(max_length=20,min_length=5)