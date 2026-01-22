from pydantic import BaseModel, EmailStr, Field, constr
from typing import List, Optional

# --- EVENT MODELS ---
class Event(BaseModel):
    event_id: str
    event_name: str
    price: int
    description: Optional[str] = None
    max_participants: Optional[int] = None

# --- REGISTRATION MODELS ---

# 1. Base User Model (The fields you requested)
class RegistrationBase(BaseModel):
    enrollment_no: str
    full_name: str
    email: EmailStr
    # Basic phone validation (10 digits)
    phone: constr(min_length=10, max_length=10) 
    college: str
    department: str
    year: str

# 2. Schema for Step 2 (Event Selection)
class EventSelection(BaseModel):
    event_ids: List[str]

# 3. Full Database Model (Includes additional fields)
class RegistrationInDB(RegistrationBase):
    id: Optional[str] = Field(alias="_id")
    selected_events: List[str] = []  # Stores full event details
    total_amount: int = 0
    payment_status: str = "PENDING"   # PENDING | PAID
    created_at: Optional[str] = None