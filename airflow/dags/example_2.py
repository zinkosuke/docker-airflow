"""
## Example DAG 2.
- aaa
- bbb
"""
from datetime import datetime
from logging import getLogger
from pprint import pformat

import pendulum
from opt.default_args import default_args

from airflow.decorators import dag
from airflow.decorators import task
from airflow.operators.python import get_current_context

logger = getLogger(__name__)


@dag(
    default_args=default_args(),
    description="",
    schedule_interval="10 * * * *",
    start_date=datetime(2021, 1, 1, tzinfo=pendulum.timezone("Asia/Tokyo")),
    catchup=False,
)
def example_2():
    @task
    def task_a():
        ctx = get_current_context()
        logger.info(
            "Context **************************************************"
        )
        logger.info(pformat(ctx))
        logger.info("dag_run.conf ******************************")
        logger.info(pformat(getattr(ctx.get("dag_run"), "conf", None)))
        return {"a_return_value": "test"}

    @task
    def task_b(a_return_value: str):
        logger.info(a_return_value)

    a = task_a()
    b = task_b(a["a_return_value"])
    a >> b


dag_ = example_2()
dag_.doc_md = __doc__
