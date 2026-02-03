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
        raise HTTPException(status_code=400, detail="Enrollment number already registered")
    
    # Check for existing Email
    if await registrations_collection.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    user_doc = data.dict()
    user_doc.update({
        "selected_events": [],
        "total_amount": 0,
        "payment_status": "PENDING",
        "created_at": datetime.utcnow().isoformat()
    })

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

    if len(selection.event_ids) > 5:
        raise HTTPException(status_code=400, detail="You can only select up to 5 events")

    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid User ID format")

    user = await registrations_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.get("payment_status") == "PAID":
        raise HTTPException(status_code=400, detail="User already PAID")

    selected_ids = selection.event_ids.copy()

    # Web Treasure Hunt capacity check
    if "web-treasure-hunt" in selected_ids:
        event = await events_collection.find_one({"event_id": "web-treasure-hunt"})
        if not event:
            raise HTTPException(status_code=400, detail="Web Treasure Hunt event not found")

        current_count = await registrations_collection.count_documents({
            "selected_events": "web-treasure-hunt",
            "payment_status": "PAID"
        })

        if current_count >= event["max_participants"]:
            selected_ids.remove("web-treasure-hunt")

    events_cursor = events_collection.find({
        "event_id": {"$in": selected_ids}
    })
    found_events = await events_cursor.to_list(length=len(selected_ids))

    if len(found_events) != len(selected_ids):
        raise HTTPException(status_code=400, detail="One or more Event IDs are invalid")

    total_amount = sum(e["price"] for e in found_events)

    # Discount logic
    if len(found_events) >= 3 and total_amount >= 150:
        total_amount -= 30

    await registrations_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {
            "selected_events": selected_ids,
            "total_amount": total_amount
        }}
    )

    return {
        "message": "Events updated successfully",
        "total_amount": total_amount,
        "selected_ids": selected_ids
    }


# ==========================================
# 3. GET USER DETAIL (Receipt / Confirmation)
# ==========================================
@router.get("/{user_id}")
async def get_user_detail(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid User ID")

    user = await registrations_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.get("selected_events"):
        event_details = await events_collection.find(
            {"event_id": {"$in": user["selected_events"]}},
            {"_id": 0}
        ).to_list(length=5)
        user["event_details"] = event_details

    user["_id"] = str(user["_id"])
    return user


# ==========================================
# 4. ADMIN: MARK AS PAID
# ==========================================
@router.patch("/{user_id}/mark-paid")
async def mark_as_paid(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid User ID")

    result = await registrations_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"payment_status": "PAID"}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "Payment status updated to PAID"}


# ==========================================
# 5. ADMIN: MARK AS UNPAID
# ==========================================
@router.patch("/{user_id}/mark-unpaid")
async def mark_as_unpaid(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid User ID")

    result = await registrations_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"payment_status": "PENDING"}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "Payment status updated to PENDING"}