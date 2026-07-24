import socket
import threading
import json
import time

class GuardianSwarm:
    def __init__(self, node_id, port=5555):
        self.node_id = node_id
        self.port = port
        self.peers = {}
        self.running = False

    def start_listener(self):
        self.running = True
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("0.0.0.0", self.port))
        
        def listen():
            while self.running:
                try:
                    data, addr = server.recvfrom(1024)
                    packet = json.loads(data.decode('utf-8'))
                    peer_id = packet.get("node_id")
                    if peer_id and peer_id != self.node_id:
                        self.peers[peer_id] = {
                            "ip": addr[0],
                            "last_seen": time.time(),
                            "status": packet.get("status", "OK")
                        }
                except Exception:
                    pass

        threading.Thread(target=listen, daemon=True).start()

    def broadcast_heartbeat(self, status="OK"):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        packet = json.dumps({
            "node_id": self.node_id,
            "status": status,
            "timestamp": time.time()
        })
        try:
            client.sendto(packet.encode('utf-8'), ('<broadcast>', self.port))
        except Exception:
            # Fallback para redes que bloquean broadcast directo
            pass
        finally:
            client.close()

    def get_swarm_status(self):
        current_time = time.time()
        active_peers = {}
        for peer_id, info in self.peers.items():
            # Si un nodo no emite en 30 segundos, se marca como inactivo
            if current_time - info["last_seen"] < 30:
                active_peers[peer_id] = info
        return active_peers
