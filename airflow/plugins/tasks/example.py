from logging import getLogger
from pprint import pformat

from base import operators

logger = getLogger(__name__)


def task_sample(*args, **kwargs):
    logger.info("args **************************************************")
    logger.info(pformat(args))
    logger.info("kwargs **************************************************")
    logger.info(pformat(kwargs))
    logger.info("kwargs.dag_run.conf ******************************")
    logger.info(pformat(getattr(kwargs.get("dag_run"), "conf", None)))
    return "sample"


def task_trigger(*args, **kwargs):
    t = operators.trigger_dagrun_operator(
        dag=kwargs["dag"],
        task_id=kwargs["task_instance"].task_id,
        trigger_dag_id=kwargs["params"]["trigger"],
    )
    logger.info(pformat(t))
    t.execute({"parent": "example"})


def task_branch(*args, **kwargs):
    return kwargs["params"]["branches"]["A"]


def task_short(*args, **kwargs):
    return False


def task_fail(*args, **kwargs):
    raise Exception("dummy")
