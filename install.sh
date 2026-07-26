#!/bin/bash

echo "🛡️ [CHRONOGUARDIANS] Iniciando instalación soberana..."

# 1. Verificar directorios y dependencias básicas
mkdir -p logs forensic_logs src/core src/web

# 2. Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual Python..."
    python3 -m venv venv
fi

# 3. Activar entorno e instalar requirements
echo "📥 Instalando dependencias desde requirements.txt..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 4. Configuración interactiva de Telegram
echo ""
echo "💬 Configuración de Notificaciones (Telegram)"
read -p "Introduce tu Telegram Bot Token (o presiona Enter para omitir): " BOT_TOKEN
read -p "Introduce tu Telegram Chat ID (o presiona Enter para omitir): " CHAT_ID

if [ ! -z "$BOT_TOKEN" ] && [ ! -z "$CHAT_ID" ]; then
    # Actualizar config.json con los datos ingresados
    python3 -c "
import json
with open('config.json', 'r') as f:
    cfg = json.load(f)
cfg['telegram_bot_token'] = '$BOT_TOKEN'
cfg['telegram_chat_id'] = '$CHAT_ID'
with open('config.json', 'w') as f:
    json.dump(cfg, f, indent=4)
"
    echo "✅ Credenciales de Telegram guardadas de forma segura en config.json."
fi

echo ""
echo "✨ ¡Instalación completada con éxito!"
echo "Para iniciar el agente ejecuta: source venv/bin/activate && python agent.py"
