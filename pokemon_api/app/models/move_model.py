from pokemon_api.app.controllers.database import connect_to_mongo

db = connect_to_mongo()


move_collection = db["move"]