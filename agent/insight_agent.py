import requests
import json
import os

def analyze_logs_groq(logs, api_key):
    """Analiza logs usando Groq API (gratis y rápido)"""
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

Logs a analizar:
{logs}
"""
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",  # Modelo gratuito de Groq
        "messages": [
            {"role": "system", "content": "Eres un ingeniero SRE experto en análisis de incidentes."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 1024
    }
    
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", 
                            headers=headers, 
                            json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"


def analyze_logs_ollama(logs, llm_url="http://localhost:11434/api/generate"):
    """Analiza logs usando Ollama local"""
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

Logs a analizar:
{logs}
"""
    payload = {
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(llm_url, json=payload)
    return response.json()["response"]


if __name__ == "__main__":
    # Logs de ejemplo
    logs_sample = """
2024-11-29 10:15:32 ERROR [auth-service] Connection pool exhausted: max connections 50 reached
2024-11-29 10:15:33 ERROR [auth-service] Database connection timeout after 30s
2024-11-29 10:15:35 WARN  [api-gateway] Upstream service not responding: auth-service
2024-11-29 10:15:40 ERROR [api-gateway] 502 Bad Gateway - failed to connect to auth-service
2024-11-29 10:15:45 ERROR [auth-service] java.sql.SQLException: Too many connections
"""
    
    # Opción 1: Usar Groq (recomendado - gratis)
    api_key = os.getenv("GROQ_API_KEY", "tu-api-key-aqui")
    
    if api_key and api_key != "tu-api-key-aqui":
        print("🤖 Usando Groq API...\n")
        result = analyze_logs_groq(logs_sample, api_key)
        print(result)
    else:
        print("❌ No hay GROQ_API_KEY configurada")
        print("📝 Obtén tu API key gratis en: https://console.groq.com/keys")
        print("\n💡 Luego ejecuta: export GROQ_API_KEY='tu-key'")
        print("\nO usa Ollama local con: analyze_logs_ollama(logs)")
