.PHONY: install start clean test status

install:
	@echo "🛡️ Instalando dependencias y configurando entorno..."
	./install.sh

start:
	@echo "🚀 Iniciando ChronoGuardians Agent..."
	@source venv/bin/activate && python agent.py

clean:
	@echo "🧹 Limpiando logs temporales y caché..."
	@rm -rf logs/*.log forensic_logs/*.json __pycache__ src/core/__pycache__ *.pyc
	@echo "✨ Entorno limpio."

status:
	@echo "📊 Estado actual del nodo ChronoGuardians:"
	@python3 -c "import sqlite3, os; print('DB Activa:', os.path.exists('chronoguardians.db'))"
