from fastapi import APIRouter
from app.schemas.schemas import EnergyPredictionRequest
from app.services.prediction_service import predict_energy

router = APIRouter()

@router.post("/predict")
def energy_prediction(request: EnergyPredictionRequest):
    prediction = predict_energy(request)
    return {"predicted_energy_kWh": prediction, "note": "Prediction based on current process conditions"}