from fastapi import APIRouter, HTTPException
from database import registrations_collection
from models.registration import Registration
from bson import ObjectId
from utils import generate_receipt
from datetime import datetime

router = APIRouter()
router = APIRouter(prefix="/api/registrations", tags=["Registrations"])

@router.post("/")
async def register_user(data: Registration):
    if await registrations_collection.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="Already registered")

    result = await registrations_collection.insert_one(data.dict())
    return {"id": str(result.inserted_id), "message": "Registered"}

@router.get("/{id}")
async def get_registration(id: str):
    reg = await registrations_collection.find_one({"_id": ObjectId(id)})
    if not reg:
        raise HTTPException(404, "Not found")
    reg["_id"] = str(reg["_id"])
    return reg

@router.put("/{id}/events")
async def update_events(id: str, events: list[str]):
    await registrations_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"selected_events": events}}
    )
    return {"message": "Events updated"}


@router.post("/register")
async def register_user(data: Registration):
    existing = await registrations_collection.find_one(
        {"enrollment_no": data.enrollment_no}
    )
    if existing:
        raise HTTPException(400, "Enrollment already registered")

    total = sum(e.price for e in data.events)

    doc = data.dict()
    doc["total_amount"] = total
    doc["receipt_no"] = generate_receipt()
    doc["created_at"] = datetime.utcnow()

    await registrations_collection.insert_one(doc)

    return {
        "message": "Registration successful",
        "receipt_no": doc["receipt_no"],
        "total_amount": total
    }

@router.get("/receipt/{enrollment_no}")
async def get_receipt(enrollment_no: str):
    user = await registrations_collection.find_one(
        {"enrollment_no": enrollment_no}, {"_id": 0}
    )
    if not user:
        raise HTTPException(404, "Receipt not found")

    return user
