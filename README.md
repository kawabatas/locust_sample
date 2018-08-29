# locust_sample

This is a templated deployment of [Locust](https://locust.io/) for Distributed Load testing using Kubernetes.

## 参考
- [helm/charts locust](https://github.com/helm/charts/tree/master/stable/locust)
- [GoogleCloudPlatform/distributed-load-testing-using-kubernetes](https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes)

## デプロイ
```
$ kustomize build | kubectl apply -f -
```

## 負荷試験実行
```
$ kubectl get pod -n locust
```
```
$ kubectl port-forward $POD_NAME_MASTER 8089 -n locust
```
ブラウザで `127.0.0.1:8089` へアクセス
