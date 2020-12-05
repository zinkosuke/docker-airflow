# docker-airflow
## Build
```
docker-compose build --no-cache --force-rm init
```

## Usage
1. Develop mode with single container.
```
docker run -it --rm -v `pwd`/airflow:/opt/airflow -p 8080:8080 airflow-local:latest ./scripts/unit_server.sh
```

1. Develop mode with docker-compose.
```
docker-compose up
```
