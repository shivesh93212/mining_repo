import random, datetime

def generate_sensor_data():
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "motor_power": random.uniform(150, 350),
        "vibration": random.uniform(2, 9),
        "temperature": random.uniform(50, 95),
        "feed_rate": random.uniform(0.8, 1.5)
    }