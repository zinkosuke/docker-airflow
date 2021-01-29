#!/usr/bin/env python
from airflow.api.common.experimental.pool import create_pool
from airflow.api.common.experimental.pool import delete_pool
from airflow.api.common.experimental.pool import get_pools

default_pool_name = "default_pool"
pools = [
    {
        "name": default_pool_name,
        "slots": 128,
        "description": "Default pool.",
    },
    {
        "name": "test_pool_1",
        "slots": 15,
        "description": "Test pool.",
    },
    {
        "name": "test_pool_2",
        "slots": 10,
        "description": "Test pool.",
    },
]


def main():
    print("Pools ********************")
    created_pools = set()
    for pool in pools:
        name = pool["name"]
        print(f"Create: {name}")
        create_pool(**pool)
        created_pools.add(name)
    for pool in get_pools():
        name = pool.pool
        if name == default_pool_name or name in created_pools:
            continue
        if name not in created_pools:
            print(f"Delete: {name}")
            delete_pool(name)
    return


if __name__ == "__main__":
    main()
