from pydantic import BaseModel
from typing import Optional

class SensorData(BaseModel):
    timestamp: str
    motor_power: float
    vibration: float
    temperature: float
    feed_rate: float

class EnergyPredictionRequest(BaseModel):
    motor_power: float
    vibration: float
    temperature: float
    feed_rate: float

class OptimizationRequest(BaseModel):
    current_speed: float
    current_load: float
    target_efficiency: Optional[float] = 0.9