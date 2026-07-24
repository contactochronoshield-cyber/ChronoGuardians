#!/bin/bash

echo "=================================================="
echo "   🛡️ INSTALADOR OFICIAL: CHRONO GUARDIAN"
echo "   Chrono Shield Networks - Soberanía Digital"
echo "=================================================="

# 1. Definir directorios
INSTALL_DIR="$HOME/chronoguardian"
mkdir -p "$INSTALL_DIR/core" "$INSTALL_DIR/logs"

echo "[*] Verificando entorno e instalando dependencias mínimas..."
if command -v pkg &> /dev/null; then
    pkg update -y && pkg install python -y
elif command -v apt &> /dev/null; then
    sudo apt update && sudo apt install -y python3 python3-pip
fi

# 2. Asegurar que Flask esté disponible
python3 -c "import flask" 2>/dev/null || pip install flask

echo "[+] ¡Dependencias listas!"
echo "[+] Estructura de Chrono Guardian configurada en: $INSTALL_DIR"
echo "--------------------------------------------------"
echo "Para iniciar el sistema completo, ejecuta:"
echo "cd ~/chronoguardian && python3 run.py"
echo "=================================================="
