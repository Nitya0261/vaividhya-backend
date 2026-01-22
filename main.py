from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import events, registrations, admin
from database import events_collection

# ===================== APP =====================
app = FastAPI(
    title="Vaividhya Event Registration API",
    version="1.0.0"
)

# ===================== CORS =====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===================== ROUTES =====================
app.include_router(events.router)
app.include_router(registrations.router)
app.include_router(admin.router)

# ===================== HEALTH CHECK =====================
@app.get("/")
async def root():
    return {"status": "Vaividhya backend is running 🚀"}

# ===================== DB TEST =====================
@app.get("/db-test")
async def db_test():
    await events_collection.find_one()
    return {"db": "connected"}
