# IA Generativa para DevOps: Observabilidad Cloud-Native + LLMs

Este repositorio contiene el material del workshop:

**"IA generativa para DevOps: automatizando insights y alertas con LLMs y observabilidad Cloud-Native"**

## 🎯 Objetivo

Mostrar, de forma práctica, cómo conectar un stack de observabilidad Cloud-Native(Prometheus, Loki, Grafana, Tempo opcional) con un modelo de lenguaje (LLM)
para transformar logs, métricas y trazas en:

- Explicaciones automáticas de incidentes
- Alertas enriquecidas en lenguaje natural
- Recomendaciones de mitigación
- Resúmenes de impacto para equipos DevOps, SRE y Cloud

## 🧱 Componentes principales

- **Cluster Kubernetes local**: Kind
- **Observabilidad**: Prometheus, Loki, Grafana
- **IA generativa**:
  - LLM local con Ollama (Mistral / Llama3)
  - o por API (OpenAI, Anthropic, Mistral, etc.)
- **Agente del workshop**:
  - Script Python que conecta logs/métricas con un LLM

## 📂 Estructura del repo

```bash
workshop-observability-llm/
  ├── README.md
  ├── setup/
  ├── agent/
  ├── datasets/
  └── dashboards/
```
