from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.abspath(os.path.join(BASE_DIR, "../logs/guardian_audit.log"))

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Chrono Guardian - Dashboard Soberano</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { background: #0f172a; color: #38bdf8; font-family: monospace; padding: 20px; }
        .card { background: #1e293b; padding: 20px; border-radius: 8px; border: 1px solid #334155; max-width: 600px; margin: auto; }
        h1 { font-size: 20px; color: #f8fafc; border-bottom: 1px solid #334155; padding-bottom: 10px; }
        pre { color: #4ade80; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🛡️ Chrono Guardian // Nodo Central</h1>
        <p>Estado: <b>{{ status }}</b></p>
        <p>Última métrica registrada:</p>
        <pre>{{ latest }}</pre>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    latest = "Esperando métricas..."
    status = "ONLINE"
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
            if lines:
                latest = lines[-1].strip()
    return render_template_string(TEMPLATE, latest=latest, status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
