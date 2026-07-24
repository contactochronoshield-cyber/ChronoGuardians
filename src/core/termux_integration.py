import subprocess
import json
import os

class TermuxIntegration:
    @staticmethod
    def is_termux():
        return "TERMUX_VERSION" in os.environ or os.path.exists("/data/data/com.termux")

    @classmethod
    def send_native_notification(cls, title, message):
        if not cls.is_termux():
            return False, "No se ejecuta en entorno Termux nativo."
        
        try:
            cmd = [
                "termux-notification",
                "--title", title,
                "--content", message,
                "--icon", "shield",
                "--priority", "high"
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True, "Notificación nativa enviada con éxito."
        except Exception as e:
            return False, f"Error al enviar notificación Termux: {str(e)}"

    @classmethod
    def get_device_status(cls):
        if not cls.is_termux():
            return {"status": "Not Termux"}
        
        status = {}
        try:
            battery = subprocess.run(["termux-battery-status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if battery.returncode == 0:
                status["battery"] = json.loads(battery.stdout)
        except Exception:
            pass
            
        try:
            wifi = subprocess.run(["termux-wifi-connectioninfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if wifi.returncode == 0:
                status["wifi"] = json.loads(wifi.stdout)
        except Exception:
            pass
            
        return status
