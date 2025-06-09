from pokemon_api.app.controllers.database import connect_to_mongo

db = connect_to_mongo()


abilities_collection = db["abilities"]

