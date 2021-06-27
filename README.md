# Monitor Internet URLs

Monitor a list of internet URLs with Python instrumented using Prometheus and Grafana served on a Kubernetes Cluster

---

## Summary

-   A service written in Python that queries two sample urls every 5 seconds:    
    -   https://httpstat.us/200
    -   https://httpstat.us/503
-   The service checks:
    -   The external urls are up (based on http status code 200) return `1` if up, `0` if otherwise
    -   Response time in milliseconds
-   The service will run a simple http service that produces metrics (on `/metrics`) and output a Prometheus format when curling the service `/metrics` url

**Sample Response Format**:
```shell
sample_external_url_up{url="https://httpstat.us/200 "}  = 1
sample_external_url_response_ms{url="https://httpstat.us/200 "}  = [value]
sample_external_url_up{url="https://httpstat.us/503 "}  = 0
sample_external_url_response_ms{url="https://httpstat.us/503 "}  = [value]
```

## Technology Used

-   [Python3](https://www.python.org/)
-   [Prometheus](https://github.com/prometheus/client_python.git)
-   [Kubernetes](https://kubernetes.io/)
-   [Helm](https://helm.sh/)
-   [Grafana](https://grafana.com/)

---

## Set-up

1. Configure URL_LIST part in [python-monitor-url.py ](python-monitor-url.py) with URLs you wish to monitor. This is currently configured with two urls as an example.

```

    URL_LIST = ["https://httpstat.us/200", "https://httpstat.us/503"]

```

2. Build Docker image and push to repository of your choosing

```shell
docker build -t $USERNAME/pythonmonitorurls .
docker run -d --rm --name prometheus-python -p 8001:8001 $USERNAME/pythonmonitorurls
```

3. Create kubernetes cluster with 1.15+

- [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [EKS](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)


4. Use `helm3` to install Prometheus & Grafana using prometheus-operator

```shell
#Install Helm3
https://helm.sh/docs/intro/install/
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh

#Install Prometheus & Grafana
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prometheus stable/prometheus-operator
```


