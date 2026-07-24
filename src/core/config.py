import os

class Config:
    HOST = os.getenv("CHRONO_HOST", "0.0.0.0")
    PORT = int(os.getenv("CHRONO_PORT", 5000))
    DEBUG = os.getenv("CHRONO_DEBUG", "False").lower() == "true"
    
    # Umbrales de alerta
    CPU_THRESHOLD = float(os.getenv("CHRONO_CPU_THRESHOLD", 85.0))
    RAM_THRESHOLD = float(os.getenv("CHRONO_RAM_THRESHOLD", 90.0))
    DISK_THRESHOLD = float(os.getenv("CHRONO_DISK_THRESHOLD", 90.0))
    
    # Telegram
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    
    # Rate Limiting para alertas (en segundos)
    ALERT_COOLDOWN = int(os.getenv("CHRONO_ALERT_COOLDOWN", 300))
