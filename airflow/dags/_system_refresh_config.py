"""
## System DAG: Refresh configurations.
- pools
- variables
"""
from datetime import datetime
from logging import getLogger

import pendulum
from airflow.api.common.experimental.pool import create_pool
from airflow.api.common.experimental.pool import delete_pool
from airflow.api.common.experimental.pool import get_pools
from airflow.decorators import dag
from airflow.decorators import task
from airflow.models import Variable
from airflow.utils.session import provide_session

from opt.default_args import default_args

logger = getLogger(__name__)


@dag(
    default_args=default_args(),
    schedule_interval="@once",
    start_date=datetime(1970, 1, 1, tzinfo=pendulum.timezone("Asia/Tokyo")),
)
def _system_refresh_config():
    @task
    def task_pools():
        new_pools = {
            "default_pool": {
                "slots": 128,
                "description": "Default pool.",
            },
            "test_pool_1": {
                "slots": 15,
                "description": "Test pool.",
            },
            "test_pool_2": {
                "slots": 10,
                "description": "Test pool.",
            },
        }
        for name, opt in new_pools.items():
            logger.info(f"Create: {name}")
            create_pool(name=name, **opt)
        for pool in get_pools():
            if pool.pool in new_pools:
                continue
            logger.info(f"Delete: {pool.pool}")
            delete_pool(pool.pool)

    @task
    @provide_session
    def task_variables(session=None):
        if session is None:
            logger.warning("Empty session.")
            return
        new_variables = {
            "test_1": "1",
            "test_2": "2",
        }
        for key, value in new_variables.items():
            logger.info(f"Create: {key}")
            Variable.set(key=key, value=value)
        for variable in session.query(Variable).all():
            if variable.key in new_variables:
                continue
            logger.info(f"Delete: {variable.key}")
            Variable.delete(variable.key)

    pools = task_pools()
    variables = task_variables()


dag_ = _system_refresh_config()
dag_.doc_md = __doc__
