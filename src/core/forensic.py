import json
import os
import time
import psutil

class ForensicEngine:
    LOG_DIR = "forensic_logs"

    @classmethod
    def capture_snapshot(cls, anomaly_data):
        if not os.path.exists(cls.LOG_DIR):
            os.makedirs(cls.LOG_DIR)
            
        timestamp = int(time.time())
        filename = os.path.join(cls.LOG_DIR, f"snapshot_{timestamp}.json")
        
        # Recolectar estado profundo para análisis posterior
        snapshot = {
            "timestamp": timestamp,
            "anomaly": anomaly_data,
            "system_load": psutil.getloadavg() if hasattr(psutil, "getloadavg") else [],
            "memory": dict(psutil.virtual_memory()._asdict()),
            "active_connections": len(psutil.net_connections()),
            "running_processes": len(psutil.pids())
        }
        
        try:
            with open(filename, "w") as f:
                json.dump(snapshot, f, indent=4)
            return filename
        except Exception as e:
            return None
