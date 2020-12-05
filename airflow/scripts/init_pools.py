#!/usr/bin/env python
from airflow.api.common.experimental.pool import create_pool

create_pool(
    name="default_pool", slots=128, description="Default pool",
)
create_pool(
    name="test_pool", slots=15, description="test_pool",
)
create_pool(
    name="test_pool2", slots=10, description="test_pool2",
)
