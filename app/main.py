from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import data_routes, predict_routes, optimize_routes
from app.database import connect_db
from app.models.energy_model import load_energy_model, MODEL_PATH
import os

# ============================================================
# 🚀 APP SETUP
# ============================================================
app = FastAPI(
    title="SmartEnergyMine API",
    description="AI + IoT Energy Optimization Backend for Iron Ore Mining",
    version="1.0"
)

# ============================================================
# 🌐 CORS (Frontend Connection Fix)
# ============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later, e.g. ["https://mining-repo-3.onrender.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# 🧠 DATABASE + MODEL LOADING
# ============================================================
try:
    connect_db()
    print("✅ Database connected successfully")
except Exception as e:
    print("⚠️ Warning: could not connect to DB:", e)

_model = None
try:
    _model = load_energy_model()
    print("✅ Energy model loaded successfully")
except Exception as e:
    print("⚠️ Warning: model load/train failed:", e)

# ============================================================
# 📡 API ROUTES
# ============================================================
# ✅ Keep all API routes above frontend mount
app.include_router(data_routes.router, prefix="/api/data", tags=["Data"])
app.include_router(predict_routes.router, prefix="/api/energy", tags=["Energy Prediction"])
app.include_router(optimize_routes.router, prefix="/api/optimize", tags=["Optimization"])

# ============================================================
# 🧭 BASIC TEST ROUTES
# ============================================================
@app.get("/api/info")
def info():
    return {
        "app": "SmartEnergyMine Backend",
        "status": "running",
        "description": "AI + IoT Energy Optimization API for Mining",
        "version": "1.0"
    }

@app.get("/api/health")
def health():
    model_exists = os.path.exists(MODEL_PATH)
    return {
        "status": "ok",
        "model_loaded": _model is not None,
        "model_present": model_exists
    }

# ============================================================
# 🖥️ FRONTEND STATIC MOUNT
# ============================================================
# ✅ Must come AFTER all API routes
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")

if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
    print(f"✅ Frontend mounted successfully from: {frontend_path}")
else:
    print("⚠️ Frontend folder not found — skipping static mount.")

# ============================================================
# 🏁 ROOT ENDPOINT (Fallback)
# ============================================================
@app.get("/")
def root():
    return {
        "message": "Welcome to SmartEnergyMine API ⚡",
        "docs": "/docs",
        "info": "/api/info",
        "health": "/api/health"
    }
