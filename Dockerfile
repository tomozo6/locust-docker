FROM locustio/locust:1.0.2
LABEL maintainer=tomozo6

COPY ./scripts/ /scripts/

EXPOSE 5557 5558 8089
