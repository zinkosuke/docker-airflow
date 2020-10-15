import os
from datetime import timedelta
from typing import Dict
from typing import Optional

import pendulum
from airflow import DAG


def dag_id_rule(file: str) -> str:
    """DAG id rules.
    >>> dag_id_rule("/opt/airflow/dags/example.py")
    'example'
    """
    base, ext = os.path.splitext(os.path.basename(file))
    return base


def default_dag_builder(
    *,
    dag_file: str,
    description: str,
    schedule_interval: str,
    start_date: str,
    retries: int = 1,
    retry_delay: int = 5,
    depends_on_past: bool = False,
    catchup: bool = False,
    pool: Optional[str] = None,
    default_args: Optional[Dict] = None,
    **kwargs,
) -> DAG:
    """"""
    dag = DAG(
        dag_id_rule(dag_file),
        description=description,
        schedule_interval=schedule_interval,
        start_date=pendulum.parse(start_date),
        default_args=dict(
            owner="airflow",
            email=["airflow@example.com"],
            email_on_failure=False,
            email_on_retry=False,
            depends_on_past=depends_on_past,
            pool=(pool or "default_pool"),
            retries=retries,
            retry_delay=timedelta(minutes=float(retry_delay)),
            **(default_args or {}),
        ),
        catchup=catchup,
        **kwargs,
    )
    return dag
