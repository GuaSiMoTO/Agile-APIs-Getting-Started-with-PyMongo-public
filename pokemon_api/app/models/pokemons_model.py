from pokemon_api.app.controllers.database import connect_to_mongo


db = connect_to_mongo()

pokemon_types_collection = db["pokemon_types"]