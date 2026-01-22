from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://vaividhya2k26:vaividhya1234@cluster0.j2coack.mongodb.net/"

client = AsyncIOMotorClient(MONGO_URL)
db = client.vividhya_db

events_collection = db.events
registrations_collection = db.registrations
admins_collection = db.admins
