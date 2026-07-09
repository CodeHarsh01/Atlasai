import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["atlas"]

# Collections
positions = db["positions"]
trades = db["trades"]
run_lock = db["run_lock"]
settings = db["settings"]

print("✅ MongoDB Connected")
