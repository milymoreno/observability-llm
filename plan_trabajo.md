# 📘 **Workshop Plan – IA Generativa para DevOps y Observabilidad Cloud-Native**

**Duración:** 90 minutos

**Formato:** Workshop práctico

**Tema:** AI, ML & Data in Cloud Native

**Requerimientos:** Docker, kubectl, VS Code, Python 3.10+ o Node 18+, Ollama o API de modelo externo

**Fecha sugerida:** Sábado 29

---

## 🟦 1. Objetivo del Workshop

Este workshop enseña cómo integrar modelos de lenguaje (LLMs) con un stack de observabilidad Cloud-Native (Prometheus, Loki, Tempo, Grafana) para generar:

* Explicaciones automáticas de incidentes
* Alertas inteligentes
* Recomendaciones proactivas
* Resúmenes en lenguaje natural desde logs, métricas y trazas

Al finalizar, cada asistente tendrá **una mini-demo funcional** capaz de analizar eventos de un sistema y producir insights automatizados.

---

## 🟩 2. Plan de Trabajo Completo (Preparación del Workshop)

### 🔵 **FASE 1 — Diseño & Organización**

1. Definir alcance del workshop y flujo principal.
2. Crear estructura inicial de presentación.
3. Seleccionar herramientas del stack observability.
4. Elegir lenguaje para la demo (Python recomendado).

---

### 🟩 **FASE 2 — Preparación del Entorno Local**

1. Instalar herramientas base:
   * Docker
   * kubectl
   * Kind o Minikube
   * Python 3.10+
2. Crear cluster local con Kind.
3. Instalar Prometheus, Loki y Grafana (Helm o manifiesto).
4. Validar conexiones y dashboards básicos.

---

### 🟧 **FASE 3 — Dataset Simulado y Dashboards**

1. Crear dataset de logs y métricas simuladas.
2. Crear dashboards en Grafana:
   * Logs
   * CPU/Latencia
   * Alertas
3. Exportar dashboards en JSON para compartir.

---

### 🟥 **FASE 4 — Creación del Agente LLM**

1. Instalar y validar Ollama (modelo mistral/llama3).
2. Crear script `insight_agent.py` con:
   * Entrada de logs
   * Interpretación del LLM
   * Generación de explicación + causa + mitigación
3. Integración con Loki vía API.
4. Integración opcional con Alertmanager vía webhook.

---

### 🟫 **FASE 5 — Integración Completa**

Unir el flujo:

<pre class="overflow-visible!" data-start="2347" data-end="2421"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2347" data-end="2421"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Prometheus</span><span> / Loki / Tempo → Script Python → LLM → Insight generado
</span></span></code></div></div></pre>

Pruebas:

* Logs con errores
* Picos de CPU
* Trazas lentas
* Eventos simulados

---

### 🟪 **FASE 6 — Preparación de la Presentación**

Estructura recomendada:

* Introducción a LLM para DevOps
* Arquitectura Cloud-Native + Generative AI
* Casos reales
* Demo
* Buenas prácticas: privacidad, seguridad, filtrado
* Recursos finales

---

### 🟫 **FASE 7 — Pruebas Finales del Workshop**

* Instalar cluster desde cero
* Reinstalar stack observability
* Probar agente LLM
* Validar estabilidad en vivo
* Revisar tiempos de respuesta
* Probar plan B con dataset offline

---

### 🟦 **FASE 8 — Materiales para Participantes**

Incluye:

* Repositorio GitHub
* Manual PDF de instrucciones
* Dataset de logs y métricas
* Dashboards JSON
* Script base del agente
* Prompts recomendados
* Bonus: ejemplos de pipelines

---

### 🟩 **FASE 9 — Ejecución del Workshop**

Checklist para el día del evento:

* Verificar Docker y cluster
* Cargar dashboards
* Validar Ollama y API keys
* Tener abiertos: VS Code, terminal, Grafana
* Preparar una demo corta y estable
* Tener un dataset offline por si falla el cluster
* Cerrar con Q&A + recursos adicionales

---

## 📦 Archivos iniciales sugeridos para el repositorio

<pre class="overflow-visible!" data-start="3686" data-end="4109"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3686" data-end="4109"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>/workshop/
  ├── README.md
  ├── plan_trabajo.md   ← ESTE DOCUMENTO
  ├── setup/
  │     ├── </span><span>cluster</span><span>-kind.yaml
  │     ├── install-observability.sh
  ├── datasets/
  │     ├── logs-simulados.</span><span>log</span><span>
  │     ├── metrics-export.prom
  ├── dashboards/
  │     ├── logs-dashboard.json
  │     ├── metrics-dashboard.json
  ├── agent/
        ├── insight_agent.py
        ├── prompts/
              ├── prompt_incidente.txt
</span></span></code></div></div></pre>

---

## 🔥 ¿Qué sigue?

Dime qué quieres construir primero:

1. **Cluster Kind + instalación de Prometheus/Grafana/Loki**
2. **El agente LLM en Python**
3. **Dataset de logs simulados**
4. **Los dashboards JSON**
5. **La presentación en diapositivas**
6. **El repositorio GitHub base (te lo genero)**
