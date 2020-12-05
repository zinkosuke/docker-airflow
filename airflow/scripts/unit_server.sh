#!/bin/sh
./scripts/init.sh
airflow scheduler &
airflow webserver
