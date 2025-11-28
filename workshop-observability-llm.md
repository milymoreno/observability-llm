# 🚀 **Workshop Observability + LLM (Replica en Ubuntu)**

### Autor: *Tú mismo*

### Fecha: *Actualizable*

---

# 1. **Requerimientos del sistema**

**Ubuntu (20.04 o superior)**

**RAM mínima para Ollama + Llama 1B:** 4 GB

**RAM recomendada:** 8 GB

**Docker:** instalado

**kubectl:** instalado

**Helm:** instalado

---

# 2. **Instalar Ollama**

<pre class="overflow-visible!" data-start="973" data-end="1030"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="973" data-end="1030"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>curl -fsSL https://ollama.com/install.sh | sh
</span></span></code></div></div></pre>

Verifica:

<pre class="overflow-visible!" data-start="1043" data-end="1071"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1043" data-end="1071"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>ollama --version
</span></span></code></div></div></pre>

---

# 3. **Instalar el modelo Llama 3.2 (1B)**

El de 1B funciona perfecto en laptops.

<pre class="overflow-visible!" data-start="1163" data-end="1198"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1163" data-end="1198"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>ollama pull llama3.2:1b
</span></span></code></div></div></pre>

Probar:

<pre class="overflow-visible!" data-start="1209" data-end="1243"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1209" data-end="1243"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>ollama run llama3.2:1b
</span></span></code></div></div></pre>

---

# 4. **Instalar Kubernetes (MicroK8s o Kind)**

## Opción A (recomendada): MicroK8s

<pre class="overflow-visible!" data-start="1337" data-end="1462"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1337" data-end="1462"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>sudo snap install microk8s --classic
sudo usermod -aG microk8s </span><span>$USER</span><span>
newgrp microk8s
microk8s status --wait-ready
</span></span></code></div></div></pre>

Habilitar DNS + Storage:

<pre class="overflow-visible!" data-start="1490" data-end="1529"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1490" data-end="1529"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>microk8s </span><span>enable</span><span> dns storage
</span></span></code></div></div></pre>

Exportar kubeconfig:

<pre class="overflow-visible!" data-start="1553" data-end="1597"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1553" data-end="1597"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>microk8s config > ~/.kube/config
</span></span></code></div></div></pre>

---

# 5. **Crear namespace para observabilidad**

<pre class="overflow-visible!" data-start="1650" data-end="1700"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1650" data-end="1700"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>kubectl create namespace observability
</span></span></code></div></div></pre>

---

# 6. **Instalar Helm**

<pre class="overflow-visible!" data-start="1731" data-end="1824"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1731" data-end="1824"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
</span></span></code></div></div></pre>

---

# 7. **Agregar repositorios de observabilidad**

<pre class="overflow-visible!" data-start="1880" data-end="2054"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="1880" data-end="2054"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>helm repo add grafana https://grafana.github.io/helm-charts
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
</span></span></code></div></div></pre>

---

# 8. **Instalar Loki + Promtail**

### Loki (almacenamiento de logs)

<pre class="overflow-visible!" data-start="2130" data-end="2250"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2130" data-end="2250"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>helm upgrade --install loki grafana/loki-stack \
  --namespace observability \
  --</span><span>set</span><span> grafana.enabled=</span><span>false</span><span>
</span></span></code></div></div></pre>

### Confirmar:

<pre class="overflow-visible!" data-start="2267" data-end="2312"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2267" data-end="2312"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>kubectl get pods -n observability
</span></span></code></div></div></pre>

---

# 9. **Instalar Grafana**

<pre class="overflow-visible!" data-start="2346" data-end="2499"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2346" data-end="2499"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>helm upgrade --install grafana grafana/grafana \
  --namespace observability \
  --</span><span>set</span><span> service.type=NodePort \
  --</span><span>set</span><span> service.nodePort=32000
</span></span></code></div></div></pre>

Obtener password:

<pre class="overflow-visible!" data-start="2520" data-end="2637"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2520" data-end="2637"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>kubectl get secret --namespace observability grafana \
  -o jsonpath=</span><span>"{.data.admin-password}"</span><span> | </span><span>base64</span><span> -d
</span></span></code></div></div></pre>

Abrir Grafana en Ubuntu:

<pre class="overflow-visible!" data-start="2665" data-end="2695"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2665" data-end="2695"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//localhost:32000</span><span>
</span></span></code></div></div></pre>

---

# 10. **Instalar kube-prometheus-stack (opcional)**

<pre class="overflow-visible!" data-start="2755" data-end="2910"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2755" data-end="2910"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>helm upgrade --install kube-prometheus prometheus-community/kube-prometheus-stack \
  --namespace observability \
  --</span><span>set</span><span> grafana.enabled=</span><span>false</span><span>
</span></span></code></div></div></pre>

---

# 11. **Crear archivo `agent/insight_agent.py`**

<pre class="overflow-visible!" data-start="2967" data-end="3702"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2967" data-end="3702"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>import</span><span> requests
</span><span>import</span><span> json

</span><span>def</span><span></span><span>analyze_logs</span><span>(</span><span>llm_url, logs</span><span>):
    prompt = f"""
Eres un ingeniero SRE senior. Analiza los siguientes logs y responde:

1. ¿Qué está pasando?
2. ¿Cuál es la causa probable?
3. Nivel de severidad (bajo/medio/alto/critico)
4. Acciones recomendadas

Logs:

</span><span>{logs}</span><span>
"""

    payload = {
        </span><span>"model"</span><span>: </span><span>"llama3.2:1b"</span><span>,
        </span><span>"prompt"</span><span>: prompt,
        </span><span>"stream"</span><span>: </span><span>False</span><span>
    }

    response = requests.post(llm_url, json=payload)
    </span><span>return</span><span> response.json()

</span><span>if</span><span> __name__ == </span><span>"__main__"</span><span>:
    llm_url = </span><span>"http://localhost:11434/api/generate"</span><span>
    logs = </span><span>"ERROR 500: timeout connecting to database\nERROR connection reset"</span><span>

    result = analyze_logs(llm_url, logs)
    </span><span>print</span><span>(json.dumps(result, indent=</span><span>2</span><span>))
</span></span></code></div></div></pre>

---

# 12. **Ejecutar el agente**

<pre class="overflow-visible!" data-start="3739" data-end="3781"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3739" data-end="3781"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python3 agent/insight_agent.py
</span></span></code></div></div></pre>

---

# 13. **Enviar logs reales (opcional)**

<pre class="overflow-visible!" data-start="3829" data-end="3877"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3829" data-end="3877"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>logs = </span><span>open</span><span>(</span><span>"logs/app.log"</span><span>).read()
</span></span></code></div></div></pre>

---

# 14. **Crear dashboard en Grafana**

1. Entrar a Grafana
2. Crear un dashboard
3. Panel → Tipo **“Text”**
4. Pegar la salida JSON del agente
5. Render → Markdown

---

# 15. **Opcional: Integración completa logs → LLM**

Estructura de carpetas:

<pre class="overflow-visible!" data-start="4139" data-end="4277"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="4139" data-end="4277"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>workshop-observability-llm/
 ├ agent/
 │   └ insight_agent.py
 ├ logs/
 │   └ app.</span><span>log</span><span>
 ├ grafana/
 └ workshop-observability-llm.md
</span></span></code></div></div></pre>

---

# 16. **Comandos rápidos para levantar todo**

<pre class="overflow-visible!" data-start="4331" data-end="4437"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="4331" data-end="4437"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>microk8s start
kubectl get pods -n observability
ollama serve &
python3 agent/insight_agent.py
</span></span></code></div></div></pre>

---

# 17. **Para subir a GitHub**

<pre class="overflow-visible!" data-start="4475" data-end="4676"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="4475" data-end="4676"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git init
git add .
git commit -m </span><span>"Observability + LLM workshop"</span><span>
git branch -M main
git remote add origin https://github.com/TU-USUARIO/workshop-observability-llm.git
git push -u origin main
</span></span></code></div></div></pre>

---

# 18. **Notas finales**

* En Windows tenías restricciones corporativas → ahora en Ubuntu todo funciona 100%.
* Puedes usar este archivo como blueprint.
* Puedes mostrar el agente funcionando en tu demo.
* No necesitas Kubernetes para ejecutar el LLM → solo para Loki/Grafana.

---
