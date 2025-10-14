import random

def optimize_parameters(current_speed, current_load, target_efficiency=0.9):
    optimized_speed = current_speed * (1 - random.uniform(0.05, 0.15))
    optimized_load = current_load * (1 - random.uniform(0.03, 0.10))
    energy_saving = random.uniform(8, 20)
    return {
        "optimized_speed": round(optimized_speed, 2),
        "optimized_load": round(optimized_load, 2),
        "expected_energy_saving_percent": round(energy_saving, 2),
        "target_efficiency": target_efficiency
    }