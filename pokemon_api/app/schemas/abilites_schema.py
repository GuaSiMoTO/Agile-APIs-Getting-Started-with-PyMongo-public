from pydantic import BaseModel

class abilitiesSchema(BaseModel):
    ability_id: int
    name: str
    effect: str
    

    class Config:
        orm_mode = True
