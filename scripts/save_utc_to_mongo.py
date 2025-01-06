import os
from pymongo import MongoClient
from datetime import datetime

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI")  # Read URI from environment variable
DATABASE_NAME = "YoutubeStats"
COLLECTION_NAME = "utc_times"


if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set!")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Save current UTC time
current_time = datetime.utcnow()
result = collection.insert_one({"utc_time": current_time})
print(f"Inserted document ID: {result.inserted_id}")

# Close the MongoDB connection
client.close()

