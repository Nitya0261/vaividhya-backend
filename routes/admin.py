from fastapi import APIRouter, HTTPException
from database import admins_collection, registrations_collection 
from models.admin import AdminLogin
from passlib.hash import bcrypt
from bson import ObjectId

router = APIRouter(prefix="/api/admin", tags=["Admin"])

# Create admin manually once
@router.post("/create")
async def create_admin(data: AdminLogin):
    data.password = bcrypt.hash(data.password)
    await admins_collection.insert_one(data.dict())
    return {"message": "Admin created"}

@router.post("/login")
async def admin_login(data: AdminLogin):
    admin = await admins_collection.find_one({"username": data.username})
    if not admin or not bcrypt.verify(data.password, admin["password"]):
        raise HTTPException(401, "Invalid credentials")
    return {"message": "Login success"}

@router.get("/registrations")
async def all_registrations():
    regs = []
    async for r in registrations_collection.find():
        r["_id"] = str(r["_id"])
        regs.append(r)
    return regs

@router.delete("/registrations/{id}")
async def delete_registration(id: str):
    await registrations_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted"}


router = APIRouter()

@router.get("/admin")
def admin_check():
    return {"message": "Admin route working"}
