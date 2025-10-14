from app.models.maintenance_model import check_machine_health

def maintenance_status(data):
    # data can be pydantic model or dict
    try:
        vibration = getattr(data, 'vibration', data.get('vibration'))
        temperature = getattr(data, 'temperature', data.get('temperature'))
    except Exception:
        # fallback defaults
        vibration = 0
        temperature = 0
    return check_machine_health(vibration, temperature)
