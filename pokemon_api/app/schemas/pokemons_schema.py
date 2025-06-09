from pydantic import BaseModel

class pokemons_Schema(BaseModel):
    pokemon_id: str
    name: str
    types: int
    abilities: str

    class Config:
        orm_mode = True
