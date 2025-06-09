
from fastapi import FastAPI
from pokemon_api.app.controllers.database import connect_to_mongo, close_mongo_connection

# Create the FastAPI application instance
app = FastAPI()
