import time
import json
import os
import sys

# Asegurar ruta src
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.core.monitor import SystemMonitor
from src.core.detector import AnomalyDetector
from src.core.notifier import TelegramNotifier
from src.core.database import ChronoDatabase
from src.core.utils import setup_logger

logger = setup_logger()

def load_config():
    if os.path.exists("config.json"):
        try:
            with open("config.json", "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "node_name": "Chrono-Node",
        "check_interval_seconds": 10,
        "log_path": "logs/guardian_audit.log"
    }

def main():
    config = load_config()
    logger.info(f"Iniciando ChronoGuardians Agent en nodo: {config.get('node_name')}")
    
    # Inicializar DB
    ChronoDatabase.init_db()
    
    log_dir = os.path.dirname(config.get("log_path", "logs/guardian_audit.log"))
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    while True:
        try:
            # 1. Recolectar métricas con psutil
            metrics = SystemMonitor.get_metrics()
            cpu = metrics["cpu"]["total"]
            ram = metrics["memory"]["percent"]
            disk = metrics["disk"]["percent"]
            
            # 2. Guardar en Historial SQLite
            ChronoDatabase.save_metric(cpu, ram, disk)
            
            # 3. Evaluar anomalías
            alerts = AnomalyDetector.evaluate(metrics)
            
            # 4. Procesar alertas y notificar
            if alerts:
                for alert in alerts:
                    msg = f"[{config.get('node_name')}] {alert['message']}"
                    logger.warning(msg)
                    if config.get("enable_telegram", True):
                        TelegramNotifier.send_alert(msg, level=alert["level"])
            else:
                logger.info(f"Métricas estables - CPU: {cpu}% | RAM: {ram}% | Disco: {disk}%")
                
            time.sleep(config.get("check_interval_seconds", 10))
            
        except KeyboardInterrupt:
            logger.info("Agente detenido por el usuario.")
            break
        except Exception as e:
            logger.error(f"Error en el ciclo del agente: {str(e)}")
            time.sleep(5)

if __name__ == "__main__":
    main()
