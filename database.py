from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is not set")

client = AsyncIOMotorClient(MONGO_URI)
db = client["vaividhya_db"]

events_collection = db["events"]
registrations_collection = db["registrations"]
admins_collection = db["admins"]

