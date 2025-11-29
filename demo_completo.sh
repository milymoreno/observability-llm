#!/bin/bash

echo "🚀 DEMO COMPLETO - Sin Grafana, Sin Kubernetes"
echo "================================================"
echo ""

# Verificar API key
if [ -z "$GROQ_API_KEY" ]; then
    echo "❌ ERROR: GROQ_API_KEY no configurada"
    echo ""
    echo "👉 Configúrala con:"
    echo "   export GROQ_API_KEY='tu_key_aqui'"
    echo ""
    echo "👉 Obtén tu key gratis en: https://console.groq.com/keys"
    exit 1
fi

echo "✅ API Key configurada"
echo ""

# Paso 1: Generar logs
echo "📝 PASO 1: Generando logs de incidente..."
echo "=========================================="
python3 datasets/generate_logs.py << EOF > datasets/sample_logs.txt 2>&1 &
1
EOF

PID=$!
sleep 3
echo "✅ Logs generándose (PID: $PID)..."
sleep 7
kill $PID 2>/dev/null || true
wait $PID 2>/dev/null || true

echo ""
echo "📊 Logs generados (primeras 20 líneas):"
echo "----------------------------------------"
grep -E "(ERROR|WARN|CRITICAL)" datasets/sample_logs.txt | head -20

echo ""
echo ""

# Paso 2: Analizar con LLM
echo "🤖 PASO 2: Analizando con el Agente LLM..."
echo "==========================================="
echo ""

python3 agent/insight_agent.py datasets/sample_logs.txt

echo ""
echo ""
echo "✅ DEMO COMPLETADA"
echo "=================="
echo ""
echo "💡 Para tu workshop:"
echo "   1. Abre: xdg-open dashboard.html (visualización)"
echo "   2. Ejecuta: bash demo_completo.sh (análisis automático)"
echo "   3. Explica cómo el LLM identifica problemas sin reglas"
echo ""
