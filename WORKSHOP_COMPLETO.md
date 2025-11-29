# 🚀 WORKSHOP COMPLETO: Observability + LLM

## Multiplataforma: Windows | Linux | macOS

---

## 📋 Quick Start (3 pasos, 5 minutos)

### 1️⃣ Obtener API Key GRATIS

🔗 **https://console.groq.com/keys**

- Crea cuenta (solo email)
- Click "Create API Key"
- Copia la key (empieza con `gsk_`)

### 2️⃣ Configurar según tu Sistema

**🐧 Linux/macOS:**
```bash
export GROQ_API_KEY="gsk_tu_key_aqui"
pip3 install requests
```

**🪟 Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="gsk_tu_key_aqui"
pip install requests
```

### 3️⃣ Ejecutar Demo

**🐧 Linux/macOS:**
```bash
bash demo_completo.sh
```

**🪟 Windows:**
```cmd
demo_windows.bat
```

---

## 🎯 Escenarios Disponibles

| # | Escenario | Duración | Recomendado |
|---|-----------|----------|-------------|
| 1 | Database Connection | 30s | ⭐⭐⭐ |
| 2 | Memory Leak | 45s | ⭐⭐ |
| 3 | High Latency | 30s | ⭐⭐ |
| 4 | Disk Full | 40s | ⭐⭐ |

---

## 💡 ¿Qué hace el Agente LLM?

Analiza logs y genera automáticamente:

1. ✅ **Resumen del incidente** - Qué está pasando
2. ✅ **Causa raíz** - Por qué está pasando  
3. ✅ **Nivel de severidad** - Qué tan grave es
4. ✅ **Acciones recomendadas** - Cómo solucionarlo
5. ✅ **Información adicional** - Contexto relevante

**Todo en segundos, sin reglas predefinidas.**

---

## 🎓 Estructura del Workshop (90 min)

### 1. Introducción (15 min)
- ¿Qué es observabilidad?
- El problema: Logs complejos
- La solución: LLMs como "SRE virtuales"
- Demo rápida del agente

### 2. Demo en Vivo (30 min)
- Generar logs de incidente
- Ejecutar el agente LLM
- Analizar el output
- Probar múltiples escenarios

### 3. Hands-On (35 min)
- Participantes ejecutan el agente
- Modificar el prompt
- Crear nuevos escenarios
- Casos de uso

### 4. Q&A (10 min)
- Preguntas
- Próximos pasos
- Recursos

---

## 📦 Requisitos

✅ Python 3.7+  
✅ API Key de Groq (gratis)  
✅ 10 MB de espacio  

**NO requiere:**
❌ Kubernetes  
❌ Grafana  
❌ Prometheus  
❌ Docker  

---

## 🔧 Troubleshooting

### Error: "GROQ_API_KEY no configurada"
```bash
# Linux/macOS
export GROQ_API_KEY="tu_key"

# Windows PowerShell
$env:GROQ_API_KEY="tu_key"
```

### Error: "ModuleNotFoundError: requests"
```bash
pip install requests
```

### Error: "Python no encontrado"
- Linux: `sudo apt install python3`
- macOS: `brew install python3`
- Windows: https://www.python.org/downloads/

---

## 📁 Estructura del Repo

```
observability-llm/
├── agent/
│   └── insight_agent.py     # Agente LLM
├── datasets/
│   └── generate_logs.py     # Generador de logs
├── dashboard.html           # Dashboard visual
├── demo_completo.sh         # Demo Linux/macOS
├── demo_windows.bat         # Demo Windows
└── README.md                # Documentación
```

---

## 🚀 Ejecución Manual (Paso a Paso)

### Paso 1: Generar Logs
```bash
python datasets/generate_logs.py
# Selecciona: 1 (Database Connection)
# Espera 10 segundos, presiona Ctrl+C
```

### Paso 2: Analizar con LLM
```bash
python agent/insight_agent.py datasets/sample_logs.txt
```

### Paso 3 (Opcional): Ver Dashboard
```bash
# Linux/macOS
xdg-open dashboard.html

# Windows
start dashboard.html
```

---

## 💼 Casos de Uso Reales

- **Análisis post-mortem** - Entender incidentes pasados
- **Alertas enriquecidas** - Contexto automático en alertas
- **Onboarding** - Ayudar a nuevos DevOps/SREs
- **Reducción MTTR** - Soluciones más rápidas
- **Documentación automática** - Generar runbooks

---

## 🔗 Links Útiles

- [Groq Console](https://console.groq.com/keys) - API Keys
- [Groq Docs](https://console.groq.com/docs) - Documentación
- [GitHub Repo](#) - Código fuente

---

## ✅ Checklist Pre-Workshop

**Antes:**
- [ ] Cuenta en Groq
- [ ] GROQ_API_KEY configurada
- [ ] Python 3.7+ instalado
- [ ] `pip install requests`
- [ ] Probar demo completo
- [ ] Dashboard abierto en navegador

**Durante:**
- [ ] Compartir repo con participantes
- [ ] Compartir link de Groq
- [ ] Demo en vivo
- [ ] Mínimo 30 min hands-on

---

## 🎯 Puntos Clave a Destacar

1. **Sin reglas predefinidas** - El LLM aprende del contexto
2. **Reduce MTTR** - Análisis en segundos
3. **Multiplataforma** - Windows, Linux, macOS
4. **Sin infraestructura** - Solo Python + API key

---

## 📚 Próximos Pasos

1. Integrar con Grafana/Loki
2. Usar Ollama local
3. Crear escenarios personalizados
4. Implementar en producción

---

**¡Listo para el workshop!** ��
