import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "energy_model.pkl")

def train_dummy_model():
    # Train a simple dummy model and persist it
    X = np.random.rand(200, 4)
    y = 200 + 50 * X[:, 0] + 30 * X[:, 1] - 10 * X[:, 2] + 5 * X[:, 3]
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print("Trained and saved dummy energy model at", MODEL_PATH)

def load_energy_model():
    if not os.path.exists(MODEL_PATH):
        train_dummy_model()
    model = joblib.load(MODEL_PATH)
    return model
