from fastapi import APIRouter, HTTPException, Depends
from database import events_collection, registrations_collection
from models import Event
from typing import List

router = APIRouter(prefix="/api/events", tags=["Events"])

# --- PUBLIC ROUTE: Get All Events ---
@router.get("/", response_model=List[Event])
async def get_all_events():
    events = []
    async for event in events_collection.find():
        # Remove MongoDB _id, keep internal event_id
        if "_id" in event: 
            del event["_id"] 
        events.append(event)
    return events

# --- ADMIN ROUTE: Create Event ---
@router.post("/")
async def create_event(event: Event):
    # Check if event_id already exists
    existing = await events_collection.find_one({"event_id": event.event_id})
    if existing:
        raise HTTPException(400, "Event ID already exists")

    await events_collection.insert_one(event.dict())
    return {"message": f"Event '{event.event_name}' created successfully"}

@router.get("/web-treasure-hunt/status")
async def get_squid_game_status():
    event = await events_collection.find_one({"event_id": "web-treasure-hunt"})
    if not event:
        raise HTTPException(404, "Event not found")

    current_count = await registrations_collection.count_documents({
        "selected_events": "web-treasure-hunt"
    })

    return {
        "event_id": "web-treasure-hunt",
        "current_participants": current_count,
        "max_participants": event["max_participants"],
        "slots_left": event["max_participants"] - current_count,
        "is_full": current_count >= event["max_participants"]
    }
