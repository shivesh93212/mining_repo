from fastapi import APIRouter, HTTPException
from app.schemas.schemas import SensorData
from app.database import get_db
from app.services.maintenance_service import maintenance_status
import json, os

router = APIRouter()

@router.post("/upload")
def upload_sensor_data(data: SensorData):
    db = get_db()
    payload = data.dict()
    if db:
        db.energy_readings.insert_one(payload)
    else:
        # fallback: save to local file
        outp = os.path.join(os.path.dirname(__file__), "..", "..", "data_backup.json")
        outp = os.path.abspath(outp)
        try:
            existing = []
            if os.path.exists(outp):
                with open(outp, "r") as f:
                    existing = json.load(f)
            existing.append(payload)
            with open(outp, "w") as f:
                json.dump(existing, f, indent=2)
        except Exception as e:
            raise HTTPException(status_code=500, detail="DB not available and failed to write fallback file: " + str(e))
    health = maintenance_status(data)
    return {"message": "Data uploaded successfully", "equipment_health": health}

@router.get("/all")
def list_data():
    db = get_db()
    if db:
        data = list(db.energy_readings.find({}, {"_id": 0}))
    else:
        # read fallback
        outp = os.path.join(os.path.dirname(__file__), "..", "..", "data_backup.json")
        outp = os.path.abspath(outp)
        if os.path.exists(outp):
            with open(outp, "r") as f:
                data = json.load(f)
        else:
            data = []
    return {"data": data}
