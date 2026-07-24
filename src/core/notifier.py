import time
import requests
from src.core.config import Config

class TelegramNotifier:
    _last_alert_time = 0

    @classmethod
    def send_alert(cls, message, level="WARNING"):
        if not Config.TELEGRAM_BOT_TOKEN or not Config.TELEGRAM_CHAT_ID:
            return False, "Telegram no configurado (Faltan variables de entorno)."

        current_time = time.time()
        # Verificar Rate Limiting (Cooldown)
        if current_time - cls._last_alert_time < Config.ALERT_COOLDOWN:
            return False, "Alerta suprimida por control de frecuencia (Cooldown activo)."

        url = f"https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": Config.TELEGRAM_CHAT_ID,
            "text": f"🛡️ **CHRONOGUARDIANS [ALERTA - {level}]** 🛡️\n\n{message}",
            "parse_mode": "Markdown"
        }

        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                cls._last_alert_time = current_time
                return True, "Alerta enviada con éxito."
            else:
                return False, f"Error de Telegram API: {response.text}"
        except Exception as e:
            return False, f"Excepción al conectar con Telegram: {str(e)}"
