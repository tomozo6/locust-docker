# locust-docker
負荷試験ツール`locust`用のシナリオスクリプトです。<br>
同梱されているDockerfile使用することで、シナリオスクリプトを取り込んだ`loucst`Dockerイメージをビルドできます。<br>
またdocker-compose.yamlを使用することで、ローカル環境からでも`locust`を実行が可能です。

## Prerequisites

## Dockerイメージの作成とDockerHubへのPush
```
$ docker build -t tomozo6/locust:0.0.1 .
$ docker push tomozo6/locust:0.0.1
```

## DockerComposeでの実行
```
$ docker-compose up
```
ブラウザで localhost:8089 にアクセス。
