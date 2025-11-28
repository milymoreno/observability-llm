# Observability LLM – Setup en Ubuntu

## 1. Requisitos
- Ubuntu 20.04+  
- Docker  
- Kubernetes Kind  
- Helm  
- Python 3.9+  
- Git  

---

## 2. Instalar Docker
```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

---

## 3. Instalar Kind
```bash
curl -Lo kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
chmod +x kind
sudo mv kind /usr/local/bin/
```

---

## 4. Instalar kubectl
```bash
sudo snap install kubectl --classic
```

---

## 5. Instalar Helm
```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

---

## 6. Crear el cluster
```bash
kind create cluster --config setup/cluster-kind.yaml
```

---

## 7. Instalar stack de observabilidad
```bash
./setup/install-observability.sh
```

---

## 8. Instalar Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 9. Descargar modelo LLM
```bash
ollama pull llama3.2:1b
```

---

## 10. Ejecutar agente
```bash
python3 agent/insight_agent.py
```

---

## 11. Acceder a Grafana
```bash
kubectl -n observability port-forward svc/kube-prometheus-grafana 3000:80
```

Grafana: http://localhost:3000

---
