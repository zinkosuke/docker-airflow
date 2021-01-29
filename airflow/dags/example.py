from logging import getLogger
from pprint import pformat

from opt.default_args import default_args

from airflow.decorators import dag
from airflow.decorators import task

logger = getLogger(__name__)


@dag(
    default_args=default_args(),
    description="",
    schedule_interval="10 * * * * *",
    start_date="2021-01-01 00:00:00",
)
def example():
    @task
    def sample(*args, **kwargs):
        logger.info("args **************************************************")
        logger.info(pformat(args))
        logger.info(
            "kwargs **************************************************"
        )
        logger.info(pformat(kwargs))
        logger.info("kwargs.dag_run.conf ******************************")
        logger.info(pformat(getattr(kwargs.get("dag_run"), "conf", None)))
