from app.models.energy_model import load_energy_model
import numpy as np

model = load_energy_model()

def predict_energy(data):
    X = np.array([[data.motor_power, data.vibration, data.temperature, data.feed_rate]])
    prediction = model.predict(X)[0]
    return round(float(prediction), 2)