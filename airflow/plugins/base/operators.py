from datetime import datetime
from datetime import timedelta
from typing import Callable
from typing import Dict
from typing import Optional

from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import ShortCircuitOperator
from airflow.utils.trigger_rule import TriggerRule

from utils.on_failure_callback import dummy_notify


def dummy_operator(*, dag: DAG, task_id: str) -> DummyOperator:
    """"""
    return DummyOperator(dag=dag, task_id=task_id)


def __base_python_operator(
    cls: PythonOperator,
    *,
    dag: DAG,
    task_id: str,
    description: str,
    params: Optional[Dict] = None,
    execution_timeout: Optional[timedelta] = None,
    on_failure_callback: Optional[Callable] = None,
    trigger_rule: Optional[str] = None,
    python_callable: Callable,
    **kwargs,
) -> PythonOperator:
    """"""
    t = cls(
        dag=dag,
        task_id=task_id,
        params=(params or {}),
        execution_timeout=(execution_timeout or timedelta(hours=1)),
        on_failure_callback=(on_failure_callback or dummy_notify),
        trigger_rule=(trigger_rule or TriggerRule.ALL_SUCCESS),
        provide_context=True,
        python_callable=python_callable,
        **kwargs,
    )
    t.doc = description
    return t


def python_operator(*args, **kwargs) -> PythonOperator:
    """"""
    return __base_python_operator(PythonOperator, **kwargs)


def branch_python_operator(*args, **kwargs) -> BranchPythonOperator:
    """"""
    return __base_python_operator(BranchPythonOperator, **kwargs)


def short_circuit_operator(*args, **kwargs) -> ShortCircuitOperator:
    """"""
    return __base_python_operator(ShortCircuitOperator, **kwargs)


def trigger_dagrun_operator(
    *,
    dag: DAG,
    task_id: str,
    trigger_dag_id: str,
    execution_date: Optional[datetime] = None,
    **kwargs,
) -> TriggerDagRunOperator:
    """"""

    def __trigger(payload: Dict, dro: TriggerDagRunOperator):
        dro.payload = payload
        return dro

    execution_date = execution_date or datetime.now()
    t = TriggerDagRunOperator(
        dag=dag,
        task_id=task_id,
        execution_date=execution_date,
        trigger_dag_id=trigger_dag_id,
        python_callable=__trigger,
        **kwargs,
    )
    return t
