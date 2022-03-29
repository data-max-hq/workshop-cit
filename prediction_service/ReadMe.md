# Getting started with k8s local cluster

## Requirements
* minikube
* kubectl
* docker

## Installing `minikube`

Installation guide is [here](https://minikube.sigs.k8s.io/docs/start/).

### MacOS
```shell
brew install minikube
```

## Installing `kubectl`

Detailed installation guide [here](https://kubernetes.io/docs/tasks/tools/).

### MacOS
```shell
brew install kubectl
```

## Install `docker`
Install docker for your OS from [here](https://docs.docker.com/get-docker/).
``
## Getting started

### Start local k8s cluster
```shell
minikube start --memory 5000 --cpus 2 \
--driver=docker --kubernetes-version=v1.21.6 \
--mount
```

### Check the installation
Open kubernetes dashboard:
```shell
minikube dashboard
```

### Build Docker image
#### locally
```shell
cd docker
docker build -t email-classifier .
minikube image load email-classifier
```

### Install the application (outside of minikube)
```shell
kubectl apply -f deployment.yaml
```
1. creates namespace: `email-classifier-namespace`
2. creates service: `flask-service`
3. creates deployment: `email-classifier-deployment`

### Make application reachable
```shell
kubectl port-forward svc/flask-service 5000:5000
```
At `localhost:5000` you should see the hello message.

### Send request

```shell
curl --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
"message": "this is a message for the legal team"
}'
```

### Change replica count
Change line 32 in `deployment.yaml`.
```shell
kubectl apply -f deployment.yaml
```

### Clean up
```shell
minikube delete
```