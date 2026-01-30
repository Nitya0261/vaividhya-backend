from fastapi import APIRouter, HTTPException
from database import registrations_collection, events_collection
from models import RegistrationBase, EventSelection
from bson import ObjectId
from datetime import datetime

router = APIRouter(prefix="/api/registrations", tags=["Registrations"])

# ==========================================
# 1. CREATE USER (Step 1: Personal Info)
# ==========================================
@router.post("/")
async def register_user_step1(data: RegistrationBase):
    # Check for existing Enrollment Number
    if await registrations_collection.find_one({"enrollment_no": data.enrollment_no}):
        raise HTTPException(400, "Enrollment number already registered")
    
    # Check for existing Email
    if await registrations_collection.find_one({"email": data.email}):
        raise HTTPException(400, "Email already registered")

    # Prepare the document for MongoDB
    user_doc = data.dict()
    user_doc.update({
        "selected_events": [],  # Initialized as empty list of strings
        "total_amount": 0,
        "payment_status": "PENDING",
        "created_at": datetime.utcnow().isoformat()
    })

    # Insert into Database
    result = await registrations_collection.insert_one(user_doc)
    
    return {
        "id": str(result.inserted_id),
        "message": "User details saved successfully"
    }

# ==========================================
# 2. UPDATE USER EVENTS (Step 2: Selection)
# ==========================================
@router.put("/{user_id}/events")
async def update_user_events(user_id: str, selection: EventSelection):
    # Constraint: Maximum 3 Events
    if len(selection.event_ids) > 3:
        raise HTTPException(400, "You can only select up to 3 events.")

    # Validate MongoDB ObjectId
    if not ObjectId.is_valid(user_id):
        raise HTTPException(400, "Invalid User ID format")

    # Check if user exists
    user = await registrations_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(404, "User not found")
    
    selected_ids = selection.event_ids.copy()

    # 🦑 SPECIAL CHECK FOR WEB TREASURE HUNT
    if "web-treasure-hunt" in selected_ids:

        web_treasure_hunt_event = await events_collection.find_one({"event_id": "web-treasure-hunt"})
        if not web_treasure_hunt_event:
            raise HTTPException(400, "Web Treasure Hunt event not found")

        max_participants = web_treasure_hunt_event["max_participants"]

        current_count = await registrations_collection.count_documents({
            "selected_events": "web-treasure-hunt",
            "payment_status": "PAID"
        })

        # 🚫 If full → remove from selection
        if current_count >= max_participants:
            selected_ids.remove("web-treasure-hunt")


    # 1. Fetch Event Objects from DB
    # We need to query the events collection to get the price of each selected event
    events_cursor = events_collection.find({"event_id": {"$in": selection.event_ids}})
    found_events = await events_cursor.to_list(length=3)

    # 2. Validate that all provided Event IDs actually exist in the DB
    if len(found_events) != len(selected_ids):
        raise HTTPException(400, "One or more Event IDs are invalid or do not exist")

    # 3. Calculate Total Amount
    total_amount = sum(e["price"] for e in found_events)

    # 🎯 Apply bundle discount: 3 events for 120
    if len(found_events) == 3 and total_amount == 150:
        total_amount = 120

    # 4. Update the User Document
    # We store the list of event IDs (selection.event_ids) and the calculated total
    await registrations_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {
            "selected_events": selection.event_ids, # Stores ["E1", "E2"]
            "total_amount": total_amount
        }}
    )

    return {
        "message": "Events updated successfully", 
        "total_amount": total_amount, 
        "selected_ids": selection.event_ids
    }

# ==========================================
# 3. GET USER DETAIL (Receipt / Confirmation)
# ==========================================
@router.get("/{user_id}")
async def get_user_detail(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(400, "Invalid User ID")
        
    user = await registrations_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(404, "User not found")
    
    # Optional: Fetch full event details to send to frontend
    # This allows the frontend to show "Robo Race" instead of just "E-101"
    if user.get("selected_events"):
        event_details = await events_collection.find(
            {"event_id": {"$in": user["selected_events"]}},
            {"_id": 0}
        ).to_list(length=3)
        user["event_details"] = event_details
        
    user["_id"] = str(user["_id"])
    return user

# ==========================================
# 4. ADMIN: MARK AS PAID
# ==========================================
@router.patch("/{user_id}/mark-paid")
async def mark_as_paid(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(400, "Invalid User ID")

    result = await registrations_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"payment_status": "PAID"}}
    )

    if result.matched_count == 0:
        raise HTTPException(404, "User not found")

    return {"message": "Payment status updated to PAID"}

# ==========================================
# 4. ADMIN: MARK AS PAID
# ==========================================
@router.patch("/{user_id}/mark-unpaid")
async def mark_as_paid(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(400, "Invalid User ID")

    result = await registrations_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"payment_status": "PENDING"}}
    )

    if result.matched_count == 0:
        raise HTTPException(404, "User not found")

    return {"message": "Payment status updated to PENDING"}