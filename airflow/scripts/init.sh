#!/bin/sh
airflow users create \
    --username=admin \
    --firstname=admin \
    --lastname=admin \
    --role=Admin \
    --email=admin@example.com
./scripts/_pools.py
./scripts/_variables.py
