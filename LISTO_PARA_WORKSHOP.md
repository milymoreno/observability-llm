# ✅ WORKSHOP LISTO - Resumen Final

## 🎯 Objetivo del Workshop

**"IA Generativa para DevOps: Observabilidad Cloud-Native + LLMs"**

Enseñar a usar LLMs como "SRE virtuales" para:
- ✅ Analizar logs automáticamente
- ✅ Identificar causas raíz en segundos
- ✅ Generar recomendaciones sin reglas predefinidas
- ✅ Reducir MTTR (Mean Time To Resolution)

**Duración:** 90 minutos  
**Plataformas:** Windows, Linux, macOS  
**Requisitos:** Python 3.7+ + API Key de Groq (gratis)

---

## 📦 Estructura del Repositorio

```
observability-llm/
├── agent/
│   └── insight_agent.py          # 🤖 Agente LLM principal
├── datasets/
│   ├── generate_logs.py          # 🎭 Generador de 4 escenarios
│   └── logs-ejemplo.log          # 📝 Logs de ejemplo
├── dashboard.html                # 📊 Dashboard visual (HTML)
├── demo_completo.sh              # 🐧 Demo automatizada (Linux/macOS)
├── demo_windows.bat              # 🪟 Demo automatizada (Windows)
├── README.md                     # 📖 Documentación principal
├── PRESENTACION_WORKSHOP.md      # 🎬 Guía paso a paso del workshop
└── WORKSHOP_COMPLETO.md          # 📚 Referencia completa
```

---

## 🚀 Para Ejecutar el Workshop

### Quick Start (3 pasos):

#### 1️⃣ Obtener API Key
```
🔗 https://console.groq.com/keys
- Crea cuenta (gratis)
- Genera API key
```

#### 2️⃣ Configurar

**Linux/macOS:**
```bash
export GROQ_API_KEY="gsk_tu_key"
pip3 install requests
```

**Windows PowerShell:**
```powershell
$env:GROQ_API_KEY="gsk_tu_key"
pip install requests
```

#### 3️⃣ Ejecutar

**Linux/macOS:**
```bash
bash demo_completo.sh
```

**Windows:**
```cmd
demo_windows.bat
```

---

## 📚 Archivos del Workshop

### Para Presentar:

1. **PRESENTACION_WORKSHOP.md** ⭐
   - Guía completa paso a paso
   - Ejemplos de cada escenario
   - Ejercicios hands-on
   - Q&A y próximos pasos
   - **Úsalo como guía durante la presentación**

2. **dashboard.html**
   - Dashboard visual interactivo
   - Muestra métricas, logs y análisis
   - Abre en navegador: `xdg-open dashboard.html`

### Para Participantes:

3. **README.md**
   - Quick start rápido
   - Requisitos mínimos
   - Comandos básicos

4. **WORKSHOP_COMPLETO.md**
   - Referencia completa
   - Troubleshooting
   - Checklist pre-workshop

### Scripts de Demo:

5. **demo_completo.sh** (Linux/macOS)
   - Demo automatizada
   - Genera logs + analiza con LLM

6. **demo_windows.bat** (Windows)
   - Versión para Windows
   - Mismo flujo que el .sh

### Código:

7. **agent/insight_agent.py**
   - Agente LLM principal
   - Usa Groq API (llama-3.1-8b)
   - Modificable para personalizar

8. **datasets/generate_logs.py**
   - Generador de logs simulados
   - 4 escenarios: DB, Memory, Latency, Disk
   - Interactivo con menú

---

## 🎬 Flujo de la Presentación (90 min)

### 1. Introducción (15 min)
- Problema: Logs complejos
- Solución: LLMs como SRE virtuales
- Demo rápida (2 min)

### 2. Demo en Vivo (30 min)
- Mostrar 3 escenarios diferentes
- Explicar análisis del LLM
- Comparar resultados

### 3. Hands-On (35 min)
- Participantes ejecutan demo
- Modificar prompts
- Probar escenarios

### 4. Q&A (10 min)
- Preguntas
- Casos de uso
- Próximos pasos

---

## 🎯 Escenarios Disponibles

| # | Escenario | Problema | Duración |
|---|-----------|----------|----------|
| 1 | Database Connection | Pool agotado | 30s ⭐ |
| 2 | Memory Leak | OOM progresivo | 45s |
| 3 | High Latency | Query lenta | 30s |
| 4 | Disk Full | Sin espacio | 40s |

---

## 📊 Lo que el LLM Analiza

Para cada incidente, el agente genera:

1. **Resumen del Incidente** - ¿Qué pasó?
2. **Causa Raíz Probable** - ¿Por qué pasó?
3. **Nivel de Severidad** - ¿Qué tan grave? (BAJA/MEDIA/ALTA/CRÍTICA)
4. **Acciones Recomendadas** - ¿Cómo solucionarlo? (priorizadas)
5. **Información Adicional** - Contexto relevante

---

## 🔗 Links Importantes

- **Repositorio:** https://github.com/milymoreno/observability-llm
- **Groq Console:** https://console.groq.com/keys
- **Groq Docs:** https://console.groq.com/docs

---

## ✅ Checklist Pre-Workshop

**24 horas antes:**
- [ ] Probar `demo_completo.sh` / `demo_windows.bat`
- [ ] Verificar que el agente funciona
- [ ] Abrir `dashboard.html` en navegador
- [ ] Tener `PRESENTACION_WORKSHOP.md` abierto
- [ ] Preparar diapositivas (opcional)

**1 hora antes:**
- [ ] Probar conexión a internet
- [ ] Verificar GROQ_API_KEY funciona
- [ ] Tener terminal lista con el repo abierto
- [ ] Dashboard HTML en otra pestaña del navegador

**Inicio del workshop:**
- [ ] Compartir link del repo con participantes
- [ ] Compartir link de Groq Console
- [ ] Explicar que NO necesitan Kubernetes/Grafana
- [ ] Dar tiempo para que configuren (5-10 min)

---

## 💡 Puntos Clave a Destacar

1. **Sin reglas predefinidas** 
   - No hay if/else para cada error
   - El LLM aprende del contexto

2. **Reduce MTTR**
   - De horas a minutos
   - Análisis en segundos

3. **Multiplataforma**
   - Windows, Linux, macOS
   - Sin instalaciones complejas

4. **Extensible**
   - Modificar prompts fácilmente
   - Agregar nuevos escenarios
   - Integrar con tu stack

---

## 🚀 Después del Workshop

Los participantes pueden:

1. **Básico:** Modificar prompts y escenarios
2. **Intermedio:** Integrar con Grafana/Loki
3. **Avanzado:** Implementar en producción

---

## 📧 Soporte

- **Issues:** Abre un issue en GitHub
- **Preguntas:** README.md tiene troubleshooting
- **Mejoras:** Pull requests bienvenidos

---

## 🎉 ¡Todo Listo!

El workshop está completamente preparado y funcional:

✅ Código funcionando (agent + generator)  
✅ Dashboard visual listo  
✅ Demos automatizadas (Linux + Windows)  
✅ Documentación completa  
✅ Presentación paso a paso  
✅ Multiplataforma  
✅ Sin dependencias de K8s/Grafana  

**Solo necesitas:**
- Proyector/pantalla
- Conexión a internet
- Participantes con Python instalado
- Tu energía y entusiasmo 🚀

---

**¡Éxito en tu workshop!** 🎯
