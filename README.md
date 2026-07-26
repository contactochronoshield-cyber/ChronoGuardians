# 🛡️ ChronoGuardians 

> *Sovereign, ultra-lightweight system monitoring and anomaly detection engine optimized for Termux, Linux, and Edge nodes.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Termux Ready](https://img.shields.io/badge/Termux-First-success.svg)](https://termux.dev/)

**ChronoGuardians** no es otro monitor pesado de infraestructura. Es una herramienta de soberanía digital diseñada para correr con menos de 20 MB de RAM, con capacidad offline-first, persistencia SQLite local y alertas inteligentes con rate-limiting directo a Telegram o Webhooks.

---

## ⚡ Características Principales

* **Termux-First & Cross-Platform:** Optimizado para dispositivos móviles Android (via Termux), Raspberry Pi y servidores Linux.
* **Cero Telemetría Externa:** Tus datos se quedan en tu nodo. Sin nubes de terceros obligatorias.
* **Persistencia Ultraligera:** Motor interno en SQLite con rotación automática de datos (historial de últimas 24h sin desbordar espacio).
* **Detector de Anomalías & Rate Limiting:** Evalúa CPU, RAM y Disco en tiempo real evitando spam en tus canales de notificación.
* **CLI Integrado:** Control total desde la terminal con comandos rápidos.

---

## 🚀 Guía de Instalación Rápida

Clona el repositorio e inicia el instalador automático:

```bash
git clone [https://github.com/contactochronoshield-cyber/ChronoGuardians.git](https://github.com/contactochronoshield-cyber/ChronoGuardians.git)
cd ChronoGuardians
make install

