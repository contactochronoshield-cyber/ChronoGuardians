import threading
import time
import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BASE_DIR, "core")

def run_agent():
    print("[*] Lanzando Agente Ligero...")
    subprocess.run([sys.executable, os.path.join(CORE_DIR, "agent.py")])

def run_dashboard():
    print("[*] Lanzando Dashboard Web...")
    subprocess.run([sys.executable, os.path.join(CORE_DIR, "dashboard.py")])

if __name__ == "__main__":
    print("=== INICIANDO SISTEMA COMPLETO CHRONO GUARDIAN ===")
    t1 = threading.Thread(target=run_agent)
    t2 = threading.Thread(target=run_dashboard)
    
    t1.daemon = True
    t2.daemon = True
    
    t1.start()
    t2.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Apagando Chrono Guardian de forma segura.")
