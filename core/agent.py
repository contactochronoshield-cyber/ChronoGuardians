import os
import time
import json
from datetime import datetime

# Directorio base absoluto basado en la ubicación de este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.abspath(os.path.join(BASE_DIR, "../logs"))
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "guardian_audit.log")

def get_system_metrics():
    try:
        with open('/proc/loadavg', 'r') as f:
            load = f.read().split()[:3]
    except:
        load = ["0.0", "0.0", "0.0"]

    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            mem_info = {}
            for line in lines:
                parts = line.split(':')
                if len(parts) == 2:
                    mem_info[parts[0].strip()] = int(parts[1].strip().split()[0])
            total_mb = mem_info.get('MemTotal', 0) / 1024
            free_mb = mem_info.get('MemAvailable', mem_info.get('MemFree', 0)) / 1024
            used_mb = total_mb - free_mb
            ram_percent = round((used_mb / total_mb) * 100, 2) if total_mb > 0 else 0
    except:
        ram_percent = 0.0

    metrics = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "load_avg": load,
        "ram_used_percent": ram_percent,
        "status": "SECURE_OFFLINE_NODE"
    }
    return metrics

if __name__ == "__main__":
    print("[*] Iniciando Agente Ligero Nativo - Chrono Guardian [Chrono Shield Networks]")
    while True:
        data = get_system_metrics()
        print(f"[+] Métricas recolectadas: {json.dumps(data, indent=2)}")
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")
        time.sleep(10)
