from pydantic import BaseModel,Field
class Location(BaseModel):
    city : str = Field()
    state : str = Field()
    country : str = Field()

    class Config:
        schema_extra = {
            "example": {
                "city": "Oaxaca de Juarez",
                "state": "Oaxaca",
                "country": "Mexico",
        }
        }