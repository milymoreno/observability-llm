#!/usr/bin/env bash
set -euo pipefail

CLUSTER_NAME="observability-llm"
NAMESPACE="observability"

echo "👉 Creando cluster Kind: $CLUSTER_NAME"
kind create cluster --name "$CLUSTER_NAME" --config "$(dirname "$0")/cluster-kind.yaml"

echo "👉 Creando namespace: $NAMESPACE (si no existe)"
kubectl create namespace "$NAMESPACE" || echo "Namespace $NAMESPACE ya existe, continuando..."

echo "👉 Agregando repositorios de Helm"
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

echo "👉 Instalando kube-prometheus-stack (Prometheus + Alertmanager + Grafana)"
helm upgrade --install kube-prometheus prometheus-community/kube-prometheus-stack \
  --namespace "$NAMESPACE" \
  --set grafana.service.type=ClusterIP \
  --set prometheus.service.type=ClusterIP

echo "👉 Instalando Loki (para logs)"
helm upgrade --install loki grafana/loki-stack \
  --namespace "$NAMESPACE" \
  --set grafana.enabled=false \
  --set promtail.enabled=true

echo "✅ Stack de observabilidad desplegado en el namespace '$NAMESPACE'"

echo ""
echo "Para acceder a Grafana, ejecuta:"
echo "  kubectl -n $NAMESPACE port-forward svc/kube-prometheus-grafana 3000:80"
echo ""
echo "Luego abre: http://localhost:3000"
echo "Usuario/contraseña por defecto: admin / prom-operator"
