## Preparing

### Minikube Initialize

```shell
minikube start --nodes 2 --cpus 3 --memory 3072 -p hb
minikube addons enable ingress -p hb
```

### Download values.yaml

```shell
curl -O "https://raw.githubusercontent.com/goharbor/harbor-helm/main/values.yaml"

#  Download Entire Chart  
# helm repo add harbor https://helm.goharbor.io
# tar zxvf harbor-1.6.0.tgz
# helm fetch harbor/harbor
```

## Installation

```shell


```


1. harbor
2. hello-fastapi > MVC 설명 & ODM, ORM, Oauth