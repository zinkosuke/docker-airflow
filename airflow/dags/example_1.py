"""
## Example DAG 1.
- aaa
- bbb
"""
import os
from datetime import datetime
from logging import getLogger
from pprint import pformat

import pendulum
from opt.default_args import default_args

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import ShortCircuitOperator

logger = getLogger(__name__)
dag_id, _ = os.path.splitext(os.path.basename(__file__))


def task_sample(*args, **kwargs) -> None:
    logger.info("args **************************************************")
    logger.info(pformat(args))
    logger.info("kwargs **************************************************")
    logger.info(pformat(kwargs))
    logger.info("kwargs.dag_run.conf ******************************")
    logger.info(pformat(getattr(kwargs.get("dag_run"), "conf", None)))
    return


def task_branch(*args, **kwargs) -> str:
    return "d"


def task_stop(*args, **kwargs) -> bool:
    return False


def task_fail(*args, **kwargs) -> None:
    raise Exception("dummy")


with DAG(
    dag_id,
    default_args=default_args(),
    description="",
    schedule_interval="10 * * * * *",
    start_date=datetime(2021, 1, 1, tzinfo=pendulum.timezone("Asia/Tokyo")),
    catchup=False,
) as dag:
    dag.doc_md = __doc__

    start = DummyOperator(task_id="start")

    a = PythonOperator(
        task_id="a",
        params={},
        python_callable=task_sample,
    )

    b = BranchPythonOperator(
        task_id="b",
        params={},
        python_callable=task_branch,
    )

    c = DummyOperator(task_id="c")

    d = DummyOperator(task_id="d")

    e = ShortCircuitOperator(
        task_id="e",
        params={},
        trigger_rule="none_failed",
        python_callable=task_stop,
    )

    f = DummyOperator(task_id="f")

    g = PythonOperator(
        task_id="g",
        params={},
        python_callable=task_fail,
    )

    start >> a >> b >> [c, d] >> e >> f
    start >> g
