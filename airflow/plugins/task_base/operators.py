from datetime import datetime
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


def dummy_operator(*, dag: DAG, task_id: str) -> DummyOperator:
    """"""
    return DummyOperator(dag=dag, task_id=task_id)


def __base_python_operator(
    cls: PythonOperator,
    *,
    dag: DAG,
    task_id: str,
    description: str,
    python_callable: Callable,
    trigger_rule: Optional[str] = None,
    params: Optional[Dict] = None,
    **kwargs,
) -> PythonOperator:
    """"""
    t = cls(
        dag=dag,
        task_id=task_id,
        provide_context=True,
        python_callable=python_callable,
        params=(params or {}),
        trigger_rule=(trigger_rule or TriggerRule.ALL_SUCCESS),
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


def __trigger(payload: Dict, dro: TriggerDagRunOperator):
    """"""
    dro.payload = payload
    return dro


def trigger_dagrun_operator(
    *,
    dag: DAG,
    task_id: str,
    trigger_dag_id: str,
    execution_date: Optional[datetime] = None,
    **kwargs,
) -> TriggerDagRunOperator:
    """"""
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
