def check_machine_health(vibration, temperature):
    if vibration > 7.5 or temperature > 80:
        return "⚠️ Maintenance Required: Possible bearing wear or overheating"
    elif vibration > 5 or temperature > 70:
        return "⚠️ Warning: Monitor equipment closely"
    else:
        return "✅ Equipment operating normally"