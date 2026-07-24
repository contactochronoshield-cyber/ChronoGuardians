import requests
import os

class WebhookNotifier:
    @staticmethod
    def send_webhook(message, level="WARNING"):
        webhook_url = os.getenv("CHRONO_WEBHOOK_URL", "")
        if not webhook_url:
            return False, "Webhook URL no configurada."

        payload = {
            "content": f"🛡️ **CHRONOGUARDIANS [{level}]**\n\n{message}",
            "level": level,
            "source": "ChronoGuardians-Node"
        }

        try:
            response = requests.post(webhook_url, json=payload, timeout=5)
            if response.status_code in [200, 201, 204]:
                return True, "Webhook enviado con éxito."
            else:
                return False, f"Error en Webhook HTTP {response.status_code}"
        except Exception as e:
            return False, f"Excepción al enviar webhook: {str(e)}"
