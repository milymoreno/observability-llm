#!/bin/bash

echo "================================"
echo "  PRUEBA RÁPIDA DEL AGENTE LLM"
echo "================================"
echo ""

# Verificar API key
if [ -z "$GROQ_API_KEY" ]; then
    echo "❌ GROQ_API_KEY no está configurada"
    echo ""
    echo "Para configurarla:"
    echo "  export GROQ_API_KEY='tu_key_aqui'"
    echo ""
    echo "Obtén tu key gratis en:"
    echo "  https://console.groq.com/keys"
    exit 1
fi

echo "✅ GROQ_API_KEY configurada"
echo ""

# Generar logs de prueba
echo "📝 Paso 1: Generando logs de incidente..."
echo "-------------------------------------------"

timeout 5 python3 datasets/generate_logs.py << EOF > datasets/sample_logs.txt 2>&1 &
1
EOF

PID=$!
sleep 3
kill $PID 2>/dev/null || true
wait $PID 2>/dev/null || true

echo "✅ Logs generados en: datasets/sample_logs.txt"
echo ""

# Mostrar primeras líneas de logs
echo "📋 Primeras 15 líneas de logs:"
echo "-------------------------------------------"
grep -E "(ERROR|WARN|CRITICAL)" datasets/sample_logs.txt 2>/dev/null | head -15
echo ""

# Analizar con el agente
echo "🤖 Paso 2: Analizando con el Agente LLM..."
echo "-------------------------------------------"
echo ""

python3 agent/insight_agent.py datasets/sample_logs.txt

echo ""
echo "================================"
echo "  ✅ PRUEBA COMPLETADA"
echo "================================"
