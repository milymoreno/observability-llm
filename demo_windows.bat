@echo off
REM Demo Completo - Workshop Observability + LLM
REM Compatible con Windows 10/11

echo ==========================================
echo   Workshop: Observability + LLM
echo   Demo Automatizado para Windows
echo ==========================================
echo.

REM Verificar API key
if "%GROQ_API_KEY%"=="" (
    echo [ERROR] GROQ_API_KEY no configurada
    echo.
    echo Para configurarla:
    echo   PowerShell: $env:GROQ_API_KEY="tu_key_aqui"
    echo   CMD:        set GROQ_API_KEY=tu_key_aqui
    echo.
    echo Obten tu key gratis en: https://console.groq.com/keys
    pause
    exit /b 1
)

echo [OK] API Key configurada
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no encontrado
    echo Instala Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python instalado
echo.

REM Paso 1: Generar logs
echo ==========================================
echo   PASO 1: Generando logs de incidente
echo ==========================================
echo.
echo Ejecuta manualmente:
echo   python datasets\generate_logs.py
echo.
echo Selecciona: 1 (Database Connection)
echo Espera 10 segundos y presiona Ctrl+C
echo.
pause

REM Paso 2: Verificar que existen logs
if not exist datasets\sample_logs.txt (
    echo [AVISO] No se encontro datasets\sample_logs.txt
    echo Asegurate de haber generado los logs primero
    echo.
    pause
)

REM Paso 3: Analizar con LLM
echo.
echo ==========================================
echo   PASO 2: Analizando con el Agente LLM
echo ==========================================
echo.

python agent\insight_agent.py datasets\sample_logs.txt

echo.
echo ==========================================
echo   DEMO COMPLETADA
echo ==========================================
echo.
echo Para ver el dashboard:
echo   Abre dashboard.html en tu navegador
echo.
pause
