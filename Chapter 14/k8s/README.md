# Kubernetes samples

## Wordcount Job
kubectl apply -f job-wordcount.yml
kubectl logs job/wordcount-job
kubectl delete -f job-wordcount.yml

## Web Deployment + HPA
kubectl apply -f deployment-web.yml
kubectl apply -f hpa.yml
kubectl get deploy,svc,hpa
