import json
import os

def check_anomalies(metrics):
    # Cargar umbrales desde la config
    config_path = "../config.json"
    threshold = 85.0
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
            threshold = config.get("alert_ram_threshold_percent", 85.0)

    # Evaluar si hay anomalía en la RAM
    if metrics.get("ram_used_percent", 0) > threshold:
        return f"[!] ALERTA CRÍTICA: Uso de RAM elevado ({metrics['ram_used_percent']}%) detectado en {metrics.get('timestamp')}"
    return None
