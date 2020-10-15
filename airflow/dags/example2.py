from airflow import DAG  # NOQA: F401

from task_base import operators
from task_base.dags import default_dag_builder
from tasks import example

dag = default_dag_builder(
    dag_file=__file__,
    description="Dag example2",
    schedule_interval="@once",
    start_date="2020-10-01 00:00:00",
)

start = operators.dummy_operator(dag=dag, task_id="start")

sample = operators.python_operator(
    dag=dag,
    task_id="sample",
    description="sample",
    python_callable=example.task_sample,
    params={"sample": "sample"},
)

start >> sample
