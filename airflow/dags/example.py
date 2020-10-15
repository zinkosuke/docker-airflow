from airflow import DAG  # NOQA: F401
from airflow.utils.trigger_rule import TriggerRule

from task_base import operators
from task_base.dags import default_dag_builder
from tasks import example

dag = default_dag_builder(
    dag_file=__file__,
    description="Dag example",
    schedule_interval="0 * * * * *",
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

trigger = operators.python_operator(
    dag=dag,
    task_id="trigger",
    description="trigger",
    python_callable=example.task_trigger,
    params={"trigger": "example2"},
)

branch = operators.branch_python_operator(
    dag=dag,
    task_id="branch",
    description="branch",
    python_callable=example.task_branch,
    params={"branches": {"A": "dummy1", "B": "dummy2"}},
)

dummy1 = operators.dummy_operator(dag=dag, task_id="dummy1")

dummy2 = operators.dummy_operator(dag=dag, task_id="dummy2")

short = operators.short_circuit_operator(
    dag=dag,
    task_id="short",
    description="short",
    python_callable=example.task_short,
    trigger_fule=TriggerRule.NONE_FAILED,
)

dummy3 = operators.dummy_operator(dag=dag, task_id="dummy3")

start >> sample >> trigger
start >> sample >> branch >> [dummy1, dummy2] >> short >> dummy3
