from pydantic import BaseModel

class pokemon_types_Schema(BaseModel):
    type_id: int
    name: str
    

    class Config:
        orm_mode = True
