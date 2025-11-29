# 🚀 Workshop: Observability + LLM

> **IA Generativa para DevOps: Análisis Inteligente de Logs con LLMs**

Un agente LLM que actúa como SRE virtual, analizando logs de observabilidad y generando insights automáticos.

## ✨ Características

- 🤖 Análisis automático de logs con LLM (Groq API)
- 🎭 Generador de incidentes simulados (4 escenarios)
- 📊 Dashboard HTML interactivo
- 🌐 **Multiplataforma: Windows, Linux, macOS**
- ⚡ Sin dependencias de Kubernetes/Grafana

## 🚀 Quick Start (2 minutos)

### 1. Configurar API Key

**Linux/macOS:**
```bash
export GROQ_API_KEY="tu_key_aqui"
```

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="tu_key_aqui"
```

### 2. Instalar Dependencias

```bash
pip install requests
```

### 3. Ejecutar Demo

**Linux/macOS:**
```bash
bash demo_completo.sh
```

**Windows:**
```powershell
python datasets/generate_logs.py
# Selecciona escenario 1, espera 10 segundos, presiona Ctrl+C
python agent/insight_agent.py datasets/sample_logs.txt
```

## 📁 Estructura

```
.
├── agent/                    # Agente LLM
│   └── insight_agent.py     # Análisis automático de logs
├── datasets/                 # Generadores de logs
│   └── generate_logs.py     # 4 escenarios de incidentes
├── dashboard.html           # Dashboard de visualización
└── demo_completo.sh         # Demo automatizada
```

## 🎯 Escenarios Disponibles

1. **Database Connection Failure** - Pool de conexiones agotado ⭐
2. **Memory Leak** - Consumo progresivo de memoria
3. **High Latency** - Degradación de rendimiento
4. **Disk Full** - Espacio en disco insuficiente

## 📦 Requisitos

- Python 3.7+
- API Key de Groq (gratis en https://console.groq.com/keys)
- 10 MB de espacio

**NO requiere**: Kubernetes, Grafana, Prometheus, Docker

## 💡 ¿Qué hace el agente?

Analiza logs y genera:
1. Resumen del incidente
2. Causa raíz
3. Nivel de severidad
4. Acciones recomendadas
5. Información adicional

Todo en segundos, sin reglas predefinidas.
