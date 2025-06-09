from pydantic import BaseModel

class moveSchema(BaseModel):
    move_id: int
    name: str
    power: int
    category: str
    pp: int

    class Config:
        orm_mode = True
