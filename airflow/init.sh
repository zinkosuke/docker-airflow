#!/bin/sh
airflow users create \
    --username=admin \
    --firstname=admin \
    --lastname=admin \
    --email=admin@example.com \
    --password=admin \
    --role=Admin
./scripts/_pools.py
./scripts/_variables.py
