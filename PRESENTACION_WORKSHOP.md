# 🎯 Workshop: IA Generativa para DevOps
## Observabilidad Cloud-Native + LLMs

---

## �‍💻 Presentación

### Mildred Moreno

**Los equipos de DevOps viven ahogados en logs y alertas.**

Yo uso **IA generativa, automatización y arquitectura cloud** para transformar ese caos en claridad: causas raíz, análisis y acciones inmediatas.

**¿Quién soy?**
- 🎓 Ingeniera y Magíster en Ciencias de la Computación
- ☁️ AWS Solutions Architect Certified
- 🤖 Futura Doctora en IA
- 💼 Especialista en DevOps, Cloud y Observabilidad

**Hoy veremos cómo la IA puede revolucionar DevOps y la observabilidad.**

---

## �📌 Objetivo del Workshop

### **Aprender a usar LLMs como "SRE virtuales"**

Al final de este workshop, serás capaz de:

✅ **Analizar logs automáticamente** con IA Generativa  
✅ **Identificar causas raíz** de incidentes en segundos  
✅ **Generar recomendaciones** de solución sin reglas predefinidas  
✅ **Reducir MTTR** (Mean Time To Resolution) dramáticamente  

### **Sin necesidad de:**
❌ Instalar Kubernetes  
❌ Configurar Grafana/Prometheus  
❌ Infraestructura compleja  

**Solo necesitas:** Python + API Key gratis de Groq

---

## 📚 Agenda (90 minutos)

```
┌─────────────────────────────────────────┐
│  15 min  │  Introducción + Demo         │
├─────────────────────────────────────────┤
│  30 min  │  Demo en Vivo Completa       │
├─────────────────────────────────────────┤
│  35 min  │  Hands-On (¡Tú lo ejecutas!) │
├─────────────────────────────────────────┤
│  10 min  │  Q&A + Próximos Pasos        │
└─────────────────────────────────────────┘
```

---

## 🎬 PARTE 1: Introducción (15 min)

### El Problema Actual

**Sin LLMs:**
```
📊 Logs complejos → 😰 Analista confundido → 🕐 Horas investigando
                  → 📝 Documentación dispersa → 💸 Tiempo perdido
```

**Con LLMs:**
```
📊 Logs complejos → 🤖 LLM analiza → ⚡ Solución en segundos
                                   → 💡 Explicación clara
                                   → 🎯 Acciones priorizadas
```

### ¿Qué es Observabilidad?

Los **3 pilares:**
1. 📝 **Logs** - Qué está pasando (eventos discretos)
2. 📊 **Métricas** - Números (CPU, memoria, latencia)
3. 🔍 **Trazas** - Viaje de una request por tus servicios

### ¿Por qué LLMs?

- ✅ **Comprenden contexto** como un humano
- ✅ **No necesitan reglas** para cada tipo de error
- ✅ **Aprenden de los logs** directamente
- ✅ **Explican en lenguaje natural**

---

## � ¿Qué son los "Insights"?

### Definición

Un **insight** es una **comprensión profunda y accionable** extraída de datos complejos.

**En observabilidad tradicional:**
```
📊 Logs crudos → 🧑 Humano lee → 🤔 Humano analiza → 💭 Humano concluye
(5-30 minutos por incidente)
```

**Con LLM generando insights:**
```
📊 Logs crudos → 🤖 LLM analiza → 💡 Insight automático
(5-10 segundos)
```

### Características de un Buen Insight

1. **Accionable** ✅
   - No solo describe el problema
   - Sugiere **qué hacer** para solucionarlo

2. **Contextualizado** 📋
   - Explica **por qué** está pasando
   - Relaciona múltiples síntomas

3. **Priorizado** 🎯
   - Indica **severidad** (¿qué tan urgente?)
   - Ordena acciones por **impacto**

4. **Comprensible** 💬
   - En lenguaje natural (no código)
   - Para cualquier nivel técnico

### Ejemplo: Log vs Insight

**Log crudo:**
```
2025-11-29 10:15:32 ERROR [auth-service] Connection pool exhausted
2025-11-29 10:15:33 ERROR [auth-service] Database timeout 30s
2025-11-29 10:15:35 WARN  [api-gateway] Upstream not responding
2025-11-29 10:15:45 ERROR [auth-service] Too many connections
```

**Insight generado por LLM:**
```
🔴 CRÍTICO: Pool de conexiones a la base de datos agotado

CAUSA RAÍZ:
- Las conexiones no se liberan después de usarse (leak)
- Límite de 50 conexiones alcanzado constantemente
- Transacciones abiertas sin cerrar

IMPACTO:
- Servicio auth-service completamente no disponible
- 95% de errores en últimos 5 minutos
- Afecta a todos los usuarios (autenticación caída)

ACCIONES INMEDIATAS:
1. Reiniciar pool de conexiones del auth-service (2 min)
2. Aumentar límite temporal: 50 → 100 conexiones (5 min)
3. Revisar código que abre conexiones DB (30 min)
4. Implementar timeout más agresivo para liberar (15 min)

PREVENCIÓN:
- Monitorear conexiones abiertas por tiempo
- Alertar cuando pool > 80% ocupado
- Code review: verificar try-finally en DB access
```

**Diferencia:**
- ❌ Log: "Algo está roto con las conexiones"
- ✅ Insight: "Por qué está roto + Cómo arreglarlo + Cómo evitarlo"

---

## �🚀 PARTE 2: Demo en Vivo (30 min)

### Demo Rápida (2 minutos)

**¡Veamos el agente en acción!**

```bash
# Generar un incidente simulado
python datasets/generate_logs.py

# El agente LLM lo analiza
python agent/insight_agent.py datasets/sample_logs.txt
```

**Resultado esperado:**
```
🤖 Análisis del Agente LLM:

1. RESUMEN: Pool de conexiones a la BD agotado
2. CAUSA: Conexiones no se liberan correctamente
3. SEVERIDAD: CRÍTICA ⚠️
4. ACCIONES:
   - Reiniciar pool de conexiones
   - Aumentar límite 50 → 100
   - Revisar código que maneja conexiones
5. INFO ADICIONAL: Circuit breaker activado
```

---

### Arquitectura del Workshop

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  datasets/generate_logs.py                          │
│  (Simula incidentes realistas)                      │
│         │                                           │
│         ▼                                           │
│  📝 sample_logs.txt                                 │
│  (Logs generados)                                   │
│         │                                           │
│         ▼                                           │
│  agent/insight_agent.py                             │
│  (Analiza con LLM vía Groq API)                     │
│         │                                           │
│         ▼                                           │
│  💡 Insights + Recomendaciones                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### Escenario 1: Database Connection Failure

**Logs simulados:**
```
2025-11-29 10:15:32 ERROR [auth-service] Connection pool exhausted
2025-11-29 10:15:33 ERROR [auth-service] Database connection timeout
2025-11-29 10:15:35 WARN  [api-gateway] Upstream service not responding
2025-11-29 10:15:40 ERROR [api-gateway] 502 Bad Gateway
2025-11-29 10:15:45 ERROR [auth-service] Too many connections
```

**Análisis del LLM:**
- 🔴 **Problema:** Pool de conexiones agotado (50/50)
- 🔍 **Causa raíz:** Conexiones no se cierran (leak probable)
- ⚡ **Solución inmediata:** Reiniciar servicio
- 🛠️ **Solución permanente:** Revisar manejo de conexiones

---

### Escenario 2: Memory Leak

**Logs simulados:**
```
2025-11-29 10:20:15 WARN  [user-service] Heap usage: 85%
2025-11-29 10:20:30 WARN  [user-service] Heap usage: 92%
2025-11-29 10:20:45 ERROR [user-service] OutOfMemoryError
2025-11-29 10:20:46 CRITICAL [user-service] Service crashed
```

**Análisis del LLM:**
- 🔴 **Problema:** Memory leak progresivo
- 🔍 **Causa raíz:** Objetos no se liberan del heap
- ⚡ **Solución inmediata:** Reiniciar JVM
- 🛠️ **Solución permanente:** Profiling + detectar leaks

---

### Escenario 3: High Latency

**Logs simulados:**
```
2025-11-29 10:25:10 WARN  [payment-api] Response time: 2500ms (SLA: 500ms)
2025-11-29 10:25:15 ERROR [payment-api] Database query timeout
2025-11-29 10:25:20 WARN  [payment-api] Response time: 5000ms
2025-11-29 10:25:25 CRITICAL Circuit breaker OPEN
```

**Análisis del LLM:**
- 🟠 **Problema:** Latencia 10x sobre SLA
- 🔍 **Causa raíz:** Query lenta en BD + efecto cascada
- ⚡ **Solución inmediata:** Circuit breaker activado (OK)
- 🛠️ **Solución permanente:** Optimizar query + cache

---

## 🎯 PARTE 3: Hands-On (35 min)

### ⚙️ Setup Inicial (5 min)

#### Paso 1: Obtener API Key GRATIS

🔗 **Ve a:** https://console.groq.com/keys

1. Crea cuenta con tu email
2. Click en "Create API Key"
3. Copia la key (empieza con `gsk_`)

#### Paso 2: Configurar según tu Sistema

**🐧 Si usas Linux/macOS:**
```bash
export GROQ_API_KEY="gsk_tu_key_aqui"
pip3 install requests
```

**🪟 Si usas Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="gsk_tu_key_aqui"
pip install requests
```

**🪟 Si usas Windows (CMD):**
```cmd
set GROQ_API_KEY=gsk_tu_key_aqui
pip install requests
```

#### Paso 3: Clonar el Repositorio

```bash
git clone https://github.com/milymoreno/observability-llm.git
cd observability-llm
```

**📦 Repositorio:** https://github.com/milymoreno/observability-llm

---

### 🏃 Ejercicio 1: Ejecutar Demo Completa (10 min)

**🐧 Linux/macOS:**
```bash
bash demo_completo.sh
```

**🪟 Windows:**
```cmd
demo_windows.bat
```

**¿Qué hace este script?**
1. ✅ Verifica que `GROQ_API_KEY` esté configurada
2. ✅ Genera logs del escenario 1 (Database Connection)
3. ✅ El agente LLM los analiza automáticamente
4. ✅ Muestra insights y recomendaciones

**Resultado esperado:**
```
✅ API Key configurada
📝 Generando logs de incidente...
🤖 Analizando con el Agente LLM...

════════════════════════════════════════
   ANÁLISIS DE INCIDENTE - LLM
════════════════════════════════════════

1. RESUMEN DEL INCIDENTE
   Pool de conexiones completamente agotado...

2. CAUSA PROBABLE
   Conexiones no se liberan correctamente...

3. SEVERIDAD: CRÍTICA
   ...

4. ACCIONES RECOMENDADAS
   - Inmediato: Reiniciar pool de conexiones
   - Corto plazo: Aumentar límite...
   ...
```

---

### 🏃 Ejercicio 2: Probar Diferentes Escenarios (10 min)

#### Generar logs manualmente:

```bash
python datasets/generate_logs.py
```

**Menú interactivo:**
```
Escenarios disponibles:
  1. Database Connection      ⭐ (Recomendado)
  2. Memory Leak
  3. High Latency
  4. Disk Full
  5. Todos los escenarios
  0. Salir

Selecciona un escenario (0-5): _
```

**Tu tarea:**
1. Selecciona escenario **2** (Memory Leak)
2. Espera 10-15 segundos
3. Presiona `Ctrl+C` para detener
4. Analiza con el agente:
   ```bash
   python agent/insight_agent.py datasets/sample_logs.txt
   ```
5. **Compara** el análisis con el del escenario 1

**Preguntas para reflexionar:**
- ¿El LLM identificó correctamente el problema?
- ¿Las recomendaciones son accionables?
- ¿Qué diferencias ves entre escenarios?

---

### 🏃 Ejercicio 3: Modificar el Prompt (10 min)

**Objetivo:** Personalizar el análisis del LLM

#### Abre el archivo del agente:
```bash
# Linux/macOS
nano agent/insight_agent.py

# Windows
notepad agent/insight_agent.py
```

#### Encuentra la función `analyze_logs_groq()`:

```python
def analyze_logs_groq(logs, api_key):
    prompt = f"""
    Eres un experto SRE analizando logs de producción.
    
    Analiza los siguientes logs e identifica:
    1. Resumen del incidente
    2. Causa raíz probable
    3. Nivel de severidad (BAJA/MEDIA/ALTA/CRÍTICA)
    4. Acciones recomendadas (priorizadas)
    5. Información adicional relevante
    
    LOGS:
    {logs}
    """
```

#### Modifica el prompt:

**Ejemplo 1:** Más técnico
```python
prompt = f"""
Eres un SRE senior con 10 años de experiencia.

Analiza estos logs de producción y genera:
1. Executive Summary (2 líneas)
2. Root Cause Analysis (detallado)
3. Severidad (P1/P2/P3/P4)
4. Runbook de mitigación (paso a paso)
5. Post-mortem inicial
6. Métricas afectadas

LOGS:
{logs}
"""
```

**Ejemplo 2:** Más simple
```python
prompt = f"""
Explica estos logs como si fuera para un junior developer.

¿Qué está roto? ¿Por qué? ¿Cómo arreglarlo?

LOGS:
{logs}
"""
```

#### Prueba tu modificación:
```bash
python agent/insight_agent.py datasets/sample_logs.txt
```

---

### 🏃 Ejercicio 4: Ver Dashboard Visual (5 min)

#### Abre el dashboard en tu navegador:

**🐧 Linux:**
```bash
xdg-open dashboard.html
```

**🍎 macOS:**
```bash
open dashboard.html
```

**🪟 Windows:**
```cmd
start dashboard.html
```

**¿Qué verás?**
- 📊 Métricas en tiempo real (simuladas)
- 📝 Vista de logs con colores por severidad
- 🤖 Análisis del LLM pre-cargado
- 🎨 Interfaz estilo Grafana

**Nota:** Este dashboard es HTML estático para demostración.
En producción, conectarías Grafana real con Loki/Prometheus.

---

### 📊 ¿Es posible ver logs en Grafana?

**SÍ, absolutamente.** De hecho, es el camino recomendado para producción.

#### Stack Completo de Observabilidad

```
┌────────────────────────────────────────────────────┐
│  APLICACIONES / SERVICIOS                          │
│  (Generan logs, métricas, trazas)                  │
└──────────────────┬─────────────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    ▼              ▼              ▼
┌─────────┐  ┌──────────┐  ┌───────────┐
│  LOKI   │  │PROMETHEUS│  │  TEMPO    │
│ (Logs)  │  │(Métricas)│  │ (Trazas)  │
└─────────┘  └──────────┘  └───────────┘
    │              │              │
    └──────────────┼──────────────┘
                   ▼
            ┌─────────────┐
            │   GRAFANA   │
            │(Visualiza)  │
            └──────┬──────┘
                   │
                   ▼
         ┌────────────────────┐
         │   AGENTE LLM       │
         │ (Analiza + Insight)│
         └────────────────────┘
```

#### Integración con Grafana

**1. Loki como fuente de logs**
```yaml
# grafana/datasources.yaml
apiVersion: 1
datasources:
  - name: Loki
    type: loki
    access: proxy
    url: http://loki:3100
    isDefault: true
```

**2. Query de logs en Grafana**
```logql
# LogQL (lenguaje de query de Loki)
{service="auth-service"} |= "ERROR" | json
```

**3. Trigger del agente LLM**

Cuando Grafana detecta anomalías:
```
Grafana Alerta → Webhook → Agente LLM → Análisis → Slack/PagerDuty
```

#### Flujo Completo en Producción

```
1. RECOLECCIÓN
   App → Promtail → Loki (almacena logs)

2. VISUALIZACIÓN
   Loki → Grafana (dashboards + alertas)

3. DETECCIÓN
   Grafana detecta patrón anómalo → Dispara alerta

4. ANÁLISIS IA
   Webhook llama al agente LLM con logs relevantes

5. INSIGHT
   LLM genera análisis + recomendaciones

6. NOTIFICACIÓN
   Resultado → Slack/Teams/PagerDuty con contexto completo

7. ACCIÓN
   SRE tiene causa raíz + pasos a seguir inmediatamente
```

#### ¿Por qué NO usamos Grafana en este workshop?

**Razones prácticas:**

1. **Instalación compleja** 
   - Requiere Kubernetes o Docker Compose
   - Loki + Prometheus + Grafana = 30-45 min setup
   - Participantes pueden tener problemas de permisos/red

2. **Espacio en disco**
   - Stack completo necesita 2-3 GB mínimo
   - No todos tienen espacio disponible

3. **Enfoque del workshop**
   - Queremos mostrar el **concepto** del agente LLM
   - La UI de Grafana es secundaria
   - Mejor usar tiempo en modificar prompts y entender IA

**Para producción:**
- ✅ Usa Grafana + Loki (mejor práctica)
- ✅ Configura alertas con webhooks
- ✅ Integra el agente LLM en tu pipeline

**Para este workshop:**
- ✅ Dashboard HTML muestra el concepto
- ✅ Nos enfocamos en el agente LLM
- ✅ Después pueden integrar con su Grafana existente

#### Demo Opcional: Grafana Cloud (GRATIS)

Si quieres ver Grafana real durante el workshop:

1. **Ve a:** https://grafana.com/auth/sign-up
2. **Crea cuenta** gratuita (14 días trial completo)
3. **Accede** a tu instancia cloud
4. **Crea dashboard** con logs de ejemplo

**Ventajas:**
- ✅ Listo en 5 minutos
- ✅ Sin instalación local
- ✅ Accesible desde cualquier lado
- ✅ UI profesional

**Para conectar el agente:**
```python
# En tu código
def send_to_grafana_cloud(analysis, api_key):
    # Enviar insight como anotación
    # O crear alert personalizada
    pass
```

---

## 💡 PARTE 4: Q&A + Próximos Pasos (10 min)

### 🤔 Preguntas Frecuentes

**Q: ¿Groq es gratis?**  
A: ✅ Sí, tier gratis generoso. Suficiente para desarrollo y demos.

**Q: ¿Puedo usar otro LLM?**  
A: ✅ Sí, el código está preparado para Ollama local también.

**Q: ¿Funciona en producción?**  
A: ✅ Sí, pero necesitas:
   - Rate limiting
   - Manejo de errores robusto
   - Caché de análisis
   - Monitoreo del LLM mismo

**Q: ¿Qué pasa con la privacidad de logs?**  
A: ⚠️ **Importante:**
   - Anonimiza datos sensibles antes de enviar
   - O usa Ollama local (privado al 100%)
   - Groq no entrena con tus datos

**Q: ¿Funciona para logs en español?**  
A: ✅ Sí, los LLMs son multilingües.

---

### 🚀 Próximos Pasos

#### 🔰 Nivel Básico: Personalización

1. **Modificar prompts** para tu caso de uso
2. **Crear nuevos escenarios** en `generate_logs.py`
3. **Agregar formatos de logs** específicos de tu empresa

#### 🔸 Nivel Intermedio: Integración

1. **Conectar con Grafana/Loki**
   - Loki como source de logs
   - Grafana para visualización
   - Agente LLM como webhook

2. **Automatizar análisis**
   - Trigger en cada alerta
   - Enviar análisis a Slack/Teams
   - Guardar en base de datos

3. **Usar Ollama local**
   ```bash
   # Instalar Ollama
   curl https://ollama.ai/install.sh | sh
   
   # Descargar modelo
   ollama pull llama3.2
   
   # Modificar insight_agent.py para usar Ollama
   ```

#### 🔹 Nivel Avanzado: Producción

1. **Pipeline completo**
   ```
   Logs → Loki → Alerta → Agente LLM → Slack → PagerDuty
   ```

2. **Análisis histórico**
   - Base de datos de análisis
   - Patrones recurrentes
   - Dashboard de insights

3. **Fine-tuning**
   - Entrenar modelo con logs reales
   - Optimizar prompts con ejemplos
   - A/B testing de modelos

---

### 📚 Recursos Adicionales

#### 🔗 Links Útiles

- **Repositorio:** https://github.com/milymoreno/observability-llm
- **Groq API:** https://console.groq.com/keys
- **Groq Docs:** https://console.groq.com/docs/quickstart
- **Ollama:** https://ollama.ai/
- **Loki Docs:** https://grafana.com/docs/loki/

#### 📖 Documentación del Repo

- `README.md` - Inicio rápido
- `WORKSHOP_COMPLETO.md` - Esta presentación
- `agent/insight_agent.py` - Código del agente (comentado)
- `datasets/generate_logs.py` - Generador de logs

#### 🎥 Para Aprender Más

- Observability 101: https://opentelemetry.io/docs/
- LLMs for DevOps: (buscar en YouTube)
- SRE Books: https://sre.google/books/

---

### 🎯 Casos de Uso Reales

#### 1. Análisis Post-Mortem Automático
**Antes:** 2-3 horas escribiendo post-mortem  
**Con LLM:** 5 minutos + revisión humana

#### 2. Onboarding de SREs Junior
**Antes:** 6 meses aprendiendo todos los sistemas  
**Con LLM:** "Copiloto" que explica cada incidente

#### 3. Reducción de MTTR
**Antes:** 45 min promedio para resolver incidentes  
**Con LLM:** 15 min (análisis en segundos + fix)

#### 4. Alertas Enriquecidas
**Antes:** "Error 500 en payment-api"  
**Con LLM:** "Error 500 causado por timeout en BD. Pool de conexiones agotado. Aumentar límite o revisar query lenta en transactions."

#### 5. Documentación Automática
**Antes:** Runbooks desactualizados  
**Con LLM:** Runbooks generados automáticamente de análisis histórico

---

## 🏆 Resumen del Workshop

### ✅ Lo que aprendiste hoy:

1. ✅ **Qué es observabilidad** y sus 3 pilares
2. ✅ **Cómo los LLMs** pueden actuar como SRE virtuales
3. ✅ **Configurar** el agente LLM con Groq API
4. ✅ **Generar** logs simulados de incidentes realistas
5. ✅ **Analizar** logs automáticamente
6. ✅ **Modificar** prompts para personalizar análisis
7. ✅ **Visualizar** en dashboard HTML

### 🎯 Puntos Clave

- 💡 **LLMs comprenden contexto** sin reglas predefinidas
- ⚡ **Reducen MTTR** dramáticamente (horas → minutos)
- 🌐 **Multiplataforma** (Windows, Linux, macOS)
- 🚀 **Sin infraestructura** compleja (solo Python + API key)
- 🔧 **Extensible** y personalizable para tu caso de uso

### 📦 Llévate a Casa

1. **Repositorio clonado:** https://github.com/milymoreno/observability-llm
2. **API Key configurada:** https://console.groq.com/keys
3. **Conocimiento:** Cómo aplicar LLMs a observabilidad
4. **Red:** Contactos de otros participantes

---

## 🙏 ¡Gracias por Participar!

### 📧 Mantente en Contacto

- **GitHub:** https://github.com/milymoreno
- **Repo del Workshop:** https://github.com/milymoreno/observability-llm
- **Issues/Preguntas:** Abre un issue en el repo

### ⭐ Si te gustó el workshop:

```bash
# Dale una estrella al repo
git clone https://github.com/milymoreno/observability-llm.git
cd observability-llm
# Abre GitHub y dale ⭐
```

### 📢 Comparte tu Experiencia

- Twitter/X: Usa #ObservabilityLLM
- LinkedIn: Comparte qué aprendiste
- Blog: Escribe sobre tu implementación

---

## 🎬 ¡Acción Final!

### Tu misión (si decides aceptarla):

1. **Esta semana:**
   - Ejecuta el workshop con logs de tu empresa (anonimizados)
   - Modifica los prompts para tu caso de uso

2. **Este mes:**
   - Integra con tu stack de observabilidad actual
   - Crea un POC (Proof of Concept) en un ambiente de staging

3. **Este trimestre:**
   - Implementa en producción
   - Mide el impacto (MTTR, satisfacción del equipo)
   - Comparte tus resultados con la comunidad

---

# 🚀 ¡Que la observabilidad y la IA te acompañen!

**Workshop creado con ❤️ para la comunidad DevOps/SRE**

*Repositorio:* https://github.com/milymoreno/observability-llm
