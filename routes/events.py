from fastapi import APIRouter
from database import events_collection
from models.event import Event

router = APIRouter(
    prefix="/api/events",
    tags=["Events"]
)

# GET all events
@router.get("/")
async def get_events():
    events = []
    async for e in events_collection.find():
        e["_id"] = str(e["_id"])
        events.append(e)
    return events

# CREATE new event
@router.post("/")
async def create_event(event: Event):
    await events_collection.insert_one(event.dict())
    return {"message": "Event created successfully"}
