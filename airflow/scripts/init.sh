#!/bin/sh
set -x
airflow initdb
./scripts/init_users.py admin admin@example.com admin
./scripts/init_pools.py
./scripts/init_variables.py
