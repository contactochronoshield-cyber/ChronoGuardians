import urllib.request
import urllib.parse
import json
import os

def send_telegram_alert(message):
    # Configuración de ejemplo para alertas soberanas vía Telegram Bot API
    # En producción esto lee de un archivo .env o config.json
    token = "TU_BOT_TOKEN_AQUI"
    chat_id = "TU_CHAT_ID_AQUI"
    
    if token == "TU_BOT_TOKEN_AQUI":
        print(f"[alerta simulada local]: {message}")
        return
        
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({'chat_id': chat_id, 'text': message}).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req) as response:
            res = response.read()
    except Exception as e:
        print(f"[!] Error enviando alerta a Telegram: {e}")
