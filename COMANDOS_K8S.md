# 🎯 Comandos Rápidos para el Workshop

## ✅ Estado del Cluster

```bash
# Ver estado del cluster
minikube status

# Ver todos los pods
kubectl get pods -n observability

# Ver logs de un pod específico
kubectl logs -n observability loki-0

# Ver eventos
kubectl get events -n observability --sort-by='.lastTimestamp'
```

---

## 🌐 Acceso a Grafana

```bash
# Port-forward (ya configurado en background)
kubectl port-forward --namespace observability service/loki-grafana 3000:80

# Credenciales:
# Usuario: admin
# Password: qRz3B5jeSNksiFQ7rXClMgrie7Vyk1Dv34nsMhA8

# URL: http://localhost:3000
```

**Navega a:** `http://localhost:3000`

---

## 📊 Grafana - Consultar Logs con LogQL

### 1. Configurar Loki como datasource

1. Ir a **Configuration** → **Data Sources**
2. Si Loki no está, agregar:
   - Tipo: Loki
   - URL: `http://loki:3100`
   - Save & Test

### 2. Queries útiles en Explore

```logql
# Ver todos los logs
{namespace="observability"}

# Logs de un pod específico
{pod="loki-0"}

# Logs con error
{namespace="observability"} |= "ERROR"

# Logs de los últimos 5 minutos con filtro
{namespace="observability"} |= "connection" | json
```

---

## 🤖 Integración con el Agente LLM

### Flujo completo:

```bash
# 1. Ver logs en Grafana
# → Ir a Explore
# → Ejecutar query LogQL
# → Copiar logs problemáticos

# 2. Guardar logs en archivo
cat > logs_incidente.txt << 'EOF'
[pegar logs de Grafana aquí]
EOF

# 3. Analizar con LLM
export GROQ_API_KEY="TU_API_KEY_AQUI"
python3 agent/insight_agent.py logs_incidente.txt

# 4. Ver análisis detallado con 9 secciones
```

---

## 🔍 Escenarios de Demo

### Escenario 1: Database Connection Issue

```bash
# 1. Generar logs
cd datasets
python3 generate_logs.py
# Seleccionar opción 1 (Database Connection)

# 2. Simular que son logs de un pod
# (En producción, vendrían de Loki via API)

# 3. Analizar con LLM
cd ..
python3 agent/insight_agent.py datasets/sample_logs.txt
```

### Escenario 2: Memory Leak

```bash
# 1. Generar logs de memory leak
cd datasets
python3 generate_logs.py
# Seleccionar opción 2 (Memory Leak)

# 2. Analizar
cd ..
python3 agent/insight_agent.py datasets/sample_logs.txt
```

---

## 🚀 Comandos para Troubleshooting

```bash
# Si un pod no arranca
kubectl describe pod <pod-name> -n observability

# Ver logs de un pod que está crasheando
kubectl logs -n observability <pod-name> --previous

# Reiniciar un deployment
kubectl rollout restart deployment loki-grafana -n observability

# Ver uso de recursos
kubectl top pods -n observability

# Eliminar y reinstalar (último recurso)
helm uninstall loki -n observability
helm install loki grafana/loki-stack -n observability \
  --set grafana.enabled=true \
  --set prometheus.enabled=true \
  --set loki.persistence.enabled=false \
  --set prometheus.server.persistentVolume.enabled=false
```

---

## 📝 Workflow Completo del Workshop

```
1. Verificar K8s
   → minikube status
   → kubectl get pods -n observability

2. Abrir Grafana
   → http://localhost:3000
   → Explorar logs con Loki

3. Generar incidente simulado
   → python3 datasets/generate_logs.py

4. Copiar logs de Grafana
   → Guardar en archivo

5. Analizar con LLM
   → export GROQ_API_KEY="..."
   → python3 agent/insight_agent.py logs.txt

6. Mostrar insights
   → 9 secciones de análisis
   → Causa raíz
   → Acciones inmediatas
```

---

## 🎯 Tips para la Presentación

1. **Tener Grafana abierto antes de empezar**
2. **Port-forward corriendo en background**
3. **API Key exportada en la terminal**
4. **Logs de ejemplo pre-generados** (por si falla algo)
5. **Dashboard HTML como backup** (si Grafana falla)

---

## ⚠️ Troubleshooting Común

### Problema: Pods en CrashLoopBackOff

```bash
# Ver qué está pasando
kubectl describe pod <pod-name> -n observability
kubectl logs <pod-name> -n observability

# Solución: Espacio en disco
df -h /
# Si está >95%, limpiar:
docker system prune -f
```

### Problema: Port-forward se cae

```bash
# Matar proceso anterior
pkill -f "port-forward"

# Reiniciar
kubectl port-forward --namespace observability \
  service/loki-grafana 3000:80 &
```

### Problema: Grafana no muestra logs

```bash
# Verificar Loki está corriendo
kubectl get pods -n observability | grep loki-0

# Verificar datasource
# Ir a Configuration → Data Sources → Loki
# URL debe ser: http://loki:3100
```

---

## 🎉 Checklist Pre-Workshop

- [ ] Minikube corriendo
- [ ] Namespace observability creado
- [ ] Pods en estado Running (wait 2-3 min)
- [ ] Port-forward a Grafana activo
- [ ] Grafana accesible en http://localhost:3000
- [ ] Loki datasource configurado
- [ ] GROQ_API_KEY exportada
- [ ] Logs de ejemplo generados
- [ ] Agente LLM probado

**Si todo está ✅ → ¡Listo para el workshop!**
