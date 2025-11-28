import requests
import json

def analyze_logs(llm_url, logs):
#     prompt = f"""
# Eres un ingeniero SRE senior. Analiza los siguientes logs y responde:

# 1. ¿Qué está pasando?
# 2. ¿Cuál es la causa probable?
# 3. Nivel de severidad (bajo/medio/alto/critico)
# 4. Acciones recomendadas

# Logs:

# {logs}
# """

    prompt = f"""
Eres un ingeniero SRE senior.

Tarea:
Analiza los siguientes logs y responde de forma breve, clara y estructurada en ESPAÑOL.

Responde SIEMPRE en este formato Markdown:

### 1. Resumen del incidente
- Descripción breve (1–2 líneas)

### 2. Causa probable
- Hipótesis principal
- Otros factores posibles (si aplica)

### 3. Severidad
- Nivel: bajo / medio / alto / crítico
- Justificación en una línea

### 4. Acciones recomendadas (máx. 4 bullets)
- Acción 1
- Acción 2
- Acción 3
- Acción 4 (opcional)

### 5. Información útil adicional (opcional)
- Solo si hay algo relevante que agregar

Logs a analizar:
{logs}
"""
    payload = {
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(llm_url, json=payload)
    return response.json()

if __name__ == "__main__":
    llm_url = "http://localhost:11434/api/generate"  # Ollama
    # logs = "ERROR 500: timeout connecting to database\nERROR connection reset"
    with open("datasets/logs-ejemplo.log", "r") as f:
        logs = f.read()
    # result = analyze_logs(llm_url, logs)
    # print(json.dumps(result, indent=2))
    result = analyze_logs(llm_url, logs)
    print(result["response"])
