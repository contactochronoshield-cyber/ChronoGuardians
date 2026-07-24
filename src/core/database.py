import sqlite3
import time
import os

class ChronoDatabase:
    DB_PATH = "chronoguardians.db"

    @classmethod
    def init_db(cls):
        conn = sqlite3.connect(cls.DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metrics_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL,
                cpu_total REAL,
                ram_percent REAL,
                disk_percent REAL
            )
        ''')
        # Mantener solo los últimos 1440 registros (aprox 24 horas si se guarda cada minuto)
        cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS clean_old_metrics
            AFTER INSERT ON metrics_history
            BEGIN
                DELETE FROM metrics_history WHERE id <= NEW.id - 1440;
            END;
        ''')
        conn.commit()
        conn.close()

    @classmethod
    def save_metric(cls, cpu, ram, disk):
        if not os.path.exists(cls.DB_PATH):
            cls.init_db()
        try:
            conn = sqlite3.connect(cls.DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO metrics_history (timestamp, cpu_total, ram_percent, disk_percent) VALUES (?, ?, ?, ?)",
                (time.time(), cpu, ram, disk)
            )
            conn.commit()
            conn.close()
        except Exception:
            pass

    @classmethod
    def get_history(cls):
        if not os.path.exists(cls.DB_PATH):
            return []
        try:
            conn = sqlite3.connect(cls.DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT timestamp, cpu_total, ram_percent, disk_percent FROM metrics_history ORDER BY timestamp ASC")
            rows = cursor.fetchall()
            conn.close()
            
            history = []
            for row in rows:
                history.append({
                    "timestamp": row[0],
                    "cpu": row[1],
                    "ram": row[2],
                    "disk": row[3]
                })
            return history
        except Exception:
            return []
