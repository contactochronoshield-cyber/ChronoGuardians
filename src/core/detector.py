from src.core.config import Config

class AnomalyDetector:
    @staticmethod
    def evaluate(metrics):
        alerts = []
        
        cpu_usage = metrics["cpu"]["total"]
        ram_usage = metrics["memory"]["percent"]
        disk_usage = metrics["disk"]["percent"]
        
        if cpu_usage >= Config.CPU_THRESHOLD:
            alerts.append({
                "level": "CRITICAL" if cpu_usage > 90.0 else "WARNING",
                "message": f"🔥 Alta carga de CPU detectada: {cpu_usage}% (Umbral: {Config.CPU_THRESHOLD}%)"
            })
            
        if ram_usage >= Config.RAM_THRESHOLD:
            alerts.append({
                "level": "CRITICAL" if ram_usage > 95.0 else "WARNING",
                "message": f"🧠 Memoria RAM al límite: {ram_usage}% (Umbral: {Config.RAM_THRESHOLD}%)"
            })
            
        if disk_usage >= Config.DISK_THRESHOLD:
            alerts.append({
                "level": "CRITICAL" if disk_usage > 95.0 else "WARNING",
                "message": f"💾 Espacio en disco crítico: {disk_usage}% (Umbral: {Config.DISK_THRESHOLD}%)"
            })
            
        return alerts
