from pprint import pprint

from task_base import operators


def task_sample(*args, **kwargs):
    print("args **************************************************")
    pprint(args)
    print("kwargs **************************************************")
    pprint(kwargs)
    print("kwargs.dag_run.conf **************************************************")
    pprint(kwargs["dag_run"].conf)
    return "sample"


def task_trigger(*args, **kwargs):
    t = operators.trigger_dagrun_operator(
        dag=kwargs["dag"],
        task_id=kwargs["task_instance"].task_id,
        trigger_dag_id=kwargs["params"]["trigger"],
    )
    pprint(t)
    t.execute({"parent": "example"})


def task_branch(*args, **kwargs):
    return kwargs["params"]["branches"]["A"]


def task_short(*args, **kwargs):
    return False
