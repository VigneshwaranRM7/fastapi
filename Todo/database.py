
from pymongo import MongoClient

# MongoDB connection string
MONGO_URI = "mongodb://localhost:27017"

# Create a MongoClient instance
client = MongoClient(MONGO_URI)

# Access the database
db = client.Todo
blogs_collection=db["set"]


def get_next_sequence(sequence_name: str) :
    counter = db["counters"].find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"sequence_value": 1}},
        upsert=True,  # Create the counter if it doesn't exist
        return_document=True
    )
    print(counter)
    return counter['sequence_value']


