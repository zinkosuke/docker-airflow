#!/bin/sh

usage() {
    cat << EOS
Usage: ./runserver.sh <command>

Commands:
  single: Init development db and start webserver and scheduler.
  webserver: Start webserver.
  scheduler: Start scheduler.
  worker: Start worker.

Environment variables:
  DJANGO_SETTINGS_MODULE : Django settings module (required).
EOS
    exit 1
}

case "${1}" in
    single)
        airflow db init
        airflow users create \
            --firstname=admin --lastname=admin --role=Admin \
            --email=admin@example.com --username=admin --password=admin
        airflow scheduler &
        airflow webserver -p 8080
        ;;
    webserver)
        airflow webserver -p 8080
        ;;
    scheduler)
        airflow scheduler
        ;;
    worker)
        airflow celery worker
        ;;
    *)
        usage
        ;;
esac
