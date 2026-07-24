import psutil
import time

class SystemMonitor:
    @staticmethod
    def get_metrics():
        # Uso de CPU total y por núcleo
        cpu_total = psutil.cpu_percent(interval=1)
        cpu_per_core = psutil.cpu_percent(interval=None, percpu=True)
        
        # Memoria RAM
        mem = psutil.virtual_memory()
        
        # Disco
        disk = psutil.disk_usage('/')
        
        # Red
        net = psutil.net_io_counters()
        
        # Procesos Top (Top 3 por uso de memoria)
        top_processes = []
        try:
            for proc in sorted(psutil.process_iter(['pid', 'name', 'memory_percent']), 
                             key=lambda p: p.info['memory_percent'] or 0.0, reverse=True)[:3]:
                top_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

        return {
            "cpu": {
                "total": cpu_total,
                "cores": cpu_per_core
            },
            "memory": {
                "total": mem.total,
                "available": mem.available,
                "percent": mem.percent
            },
            "disk": {
                "total": disk.total,
                "used": disk.used,
                "free": disk.free,
                "percent": disk.percent
            },
            "network": {
                "bytes_sent": net.bytes_sent,
                "bytes_recv": net.bytes_recv
            },
            "top_processes": top_processes,
            "timestamp": time.time()
        }
