import requests
import json
import os

def analyze_logs_groq(logs, api_key):
    """
    Analiza logs usando Groq API (llama-3.1-8b-instant)
    Genera insights estructurados y accionables
    """
    
    prompt = f"""Eres un SRE experto con 15 años de experiencia analizando incidentes de producción.

Analiza los siguientes logs y genera un análisis COMPLETO y ACCIONABLE en ESPAÑOL.

FORMATO DE RESPUESTA (usa emojis para mejor legibilidad):

### 📋 RESUMEN EJECUTIVO
(2-3 líneas explicando qué está pasando)

### 🔍 ANÁLISIS TÉCNICO
- **Síntomas observados:**
  - Síntoma 1
  - Síntoma 2
- **Componentes afectados:** [lista]
- **Patrón del error:** [descripción]

### 🎯 CAUSA RAÍZ PROBABLE
(Explica la causa más probable con evidencia de los logs)

### 🔴 SEVERIDAD
**Nivel:** BAJA / MEDIA / ALTA / CRÍTICA  
**Justificación:** (1-2 líneas)

### ⚡ ACCIONES INMEDIATAS (próximos 15 min)
1. **Acción 1:** [Descripción] (Tiempo: X min)
2. **Acción 2:** [Descripción] (Tiempo: X min)
3. **Acción 3:** [Descripción] (Tiempo: X min)

### 🛠️ SOLUCIÓN PERMANENTE
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

### 📊 IMPACTO
- **Usuarios afectados:** [estimación]
- **Funcionalidad:** [qué no funciona]
- **SLA:** [status]

### 🔮 PREVENCIÓN
- Alertas a configurar
- Métricas a monitorear
- Mejoras sugeridas

LOGS A ANALIZAR:
{logs}
"""
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Eres un SRE senior experto en análisis de incidentes y observabilidad cloud-native."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,  # Más determinístico
        "max_tokens": 2048   # Más tokens para análisis completo
    }
    
    try:
        print("🤖 Analizando logs con LLM (llama-3.1-8b-instant)...")
        print("⏳ Esto puede tomar 5-15 segundos...\n")
        
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", 
                                headers=headers, 
                                json=payload,
                                timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            analysis = result["choices"][0]["message"]["content"]
            
            # Formatear salida
            print("=" * 80)
            print("   🎯 ANÁLISIS DE INCIDENTE - INSIGHT GENERADO POR IA")
            print("=" * 80)
            print()
            print(analysis)
            print()
            print("=" * 80)
            tokens = result.get("usage", {}).get("total_tokens", "N/A")
            print(f"✅ Análisis completado | Tokens usados: {tokens}")
            print("=" * 80)
            
            return analysis
        else:
            error_msg = f"❌ ERROR {response.status_code}: {response.text}"
            print(error_msg)
            return error_msg
            
    except requests.exceptions.Timeout:
        return "❌ ERROR: Timeout al conectar con Groq API (>30s)"
    except Exception as e:
        return f"❌ ERROR inesperado: {str(e)}"


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
