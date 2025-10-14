from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import data_routes, predict_routes, optimize_routes
from app.database import connect_db
from app.models.energy_model import load_energy_model, MODEL_PATH
import os

app = FastAPI(
    title="SmartEnergyMine API",
    description="AI + IoT Energy Optimization Backend for Iron Ore Mining",
    version="1.0"
)

# ✅ Allow frontend (CORS fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict later, e.g., ["http://localhost:8080"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Try to connect to DB
try:
    connect_db()
except Exception as e:
    print("⚠️ Warning: could not connect to DB:", e)

# ✅ Preload model (train dummy if not present)
_model = None
try:
    _model = load_energy_model()
except Exception as e:
    print("⚠️ Warning: model load/train failed:", e)

# ✅ Include routes
app.include_router(data_routes.router, prefix="/api/data", tags=["Data"])
app.include_router(predict_routes.router, prefix="/api/energy", tags=["Energy Prediction"])
app.include_router(optimize_routes.router, prefix="/api/optimize", tags=["Optimization"])

# ✅ Default routes
@app.get("/")
def home():
    return {"message": "SmartEnergyMine backend is running 🚀"}

@app.get("/api/health")
def health():
    model_exists = os.path.exists(MODEL_PATH)
    return {
        "status": "ok",
        "db_connected": True if _model is not None else False,
        "model_present": model_exists
    }
