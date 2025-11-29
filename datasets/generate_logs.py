#!/usr/bin/env python3
"""
Generador de logs simulados para el workshop
Simula diferentes escenarios de incidentes
"""

import time
import random
from datetime import datetime

SCENARIOS = {
    "database_connection": [
        "ERROR [auth-service] Connection pool exhausted: max connections 50 reached",
        "ERROR [auth-service] Database connection timeout after 30s",
        "ERROR [auth-service] com.mysql.jdbc.exceptions.jdbc4.MySQLNonTransientConnectionException",
        "ERROR [auth-service] Unable to acquire JDBC Connection",
        "WARN  [api-gateway] Upstream service not responding: auth-service",
    ],
    "memory_leak": [
        "WARN  [user-service] High memory usage detected: 85%",
        "ERROR [user-service] OutOfMemoryError: Java heap space",
        "ERROR [user-service] GC overhead limit exceeded",
        "CRITICAL [monitoring] Memory usage critical: 95%",
        "ERROR [user-service] Application crashed - OOM",
    ],
    "high_latency": [
        "WARN  [api-gateway] Request latency increased: 3500ms",
        "ERROR [api-gateway] Request timeout: 60000ms exceeded",
        "WARN  [payment-service] Slow query detected: 5200ms",
        "ERROR [payment-service] Database query timeout",
        "CRITICAL [monitoring] P95 latency exceeds SLA: 8000ms",
    ],
    "disk_full": [
        "ERROR [app-service] Failed to write log file: No space left on device",
        "CRITICAL [monitoring] Disk usage: 98% on /dev/sda1",
        "ERROR [app-service] Cannot create temp file: disk full",
        "ERROR [database] Transaction log full, cannot write",
        "CRITICAL [alertmanager] Disk space critical on node-01",
    ]
}

def generate_log_line(service, level, message):
    """Genera una línea de log con timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} {level:8} [{service}] {message}"

def simulate_scenario(scenario_name, duration=10):
    """Simula un escenario de incidente"""
    logs = SCENARIOS.get(scenario_name, [])
    
    print(f"\n{'='*70}")
    print(f"🔥 Simulando incidente: {scenario_name.replace('_', ' ').upper()}")
    print(f"{'='*70}\n")
    
    for i in range(duration):
        log = random.choice(logs)
        # Extraer service del log
        if '[' in log and ']' in log:
            parts = log.split('[')
            level = parts[0].strip()
            service_msg = parts[1].split(']')
            service = service_msg[0]
            message = service_msg[1].strip()
        else:
            level = "INFO"
            service = "system"
            message = log
            
        print(generate_log_line(service, level, message))
        time.sleep(random.uniform(0.5, 2.0))
    
    print(f"\n{'='*70}\n")

def interactive_mode():
    """Modo interactivo para seleccionar escenarios"""
    print("\n🎭 Generador de Logs Simulados - Workshop Observability")
    print("="*70)
    print("\nEscenarios disponibles:")
    
    for i, (key, _) in enumerate(SCENARIOS.items(), 1):
        print(f"  {i}. {key.replace('_', ' ').title()}")
    
    print(f"  {len(SCENARIOS) + 1}. Todos los escenarios")
    print("  0. Salir")
    print("="*70)
    
    while True:
        try:
            choice = input("\nSelecciona un escenario (0-{}): ".format(len(SCENARIOS) + 1))
            choice = int(choice)
            
            if choice == 0:
                print("\n👋 ¡Hasta luego!")
                break
            elif choice == len(SCENARIOS) + 1:
                for scenario in SCENARIOS.keys():
                    simulate_scenario(scenario, duration=5)
            elif 1 <= choice <= len(SCENARIOS):
                scenario = list(SCENARIOS.keys())[choice - 1]
                simulate_scenario(scenario, duration=10)
            else:
                print("❌ Opción inválida")
        except ValueError:
            print("❌ Por favor ingresa un número")
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    interactive_mode()
