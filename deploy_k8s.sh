#!/bin/bash

# Apply the Kubernetes deployment for the backend service
kubectl apply -f backend-deployment.yml

# Apply the Kubernetes deployment for the frontend service
kubectl apply -f frontend-deployment.yml

# Expose the backend service using NodePort (or LoadBalancer for cloud-based clusters)
kubectl expose deployment backend --type=NodePort --name=backend-service --port=5000 --target-port=5000
kubectl expose deployment frontend --type=NodePort --name=frontend-service --port=80 --target-port=80

# Optionally, you can open the services using Minikube's service command
minikube service frontend --url
minikube service backend --url

