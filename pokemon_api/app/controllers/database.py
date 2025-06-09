from pymongo import MongoClient

class Database:
    client = None  

def connect_to_mongo():
    try:
        # Start the connection to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        # Select the "tienda" database
        db = client["pokemon_db"]
        print("Connection to MongoDB established successfully")
        return db
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        raise e


def close_mongo_connection():
    if Database.client:
        Database.client.close()
        print("Connection to MongoDB closed")
