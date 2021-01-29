from datetime import timedelta
from logging import getLogger
from pprint import pformat
from typing import Dict

logger = getLogger(__name__)


def dummy_notify(*args, **kwargs) -> None:
    logger.info("on_failure_callback")
    logger.info(pformat(args))
    logger.info(pformat(kwargs))


def default_args(**kwargs) -> Dict:
    return {
        "owner": "airflow",
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "depends_on_past": False,
        "pool": "default_pool",
        "execution_timeout": timedelta(hours=1),
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        "on_failure_callback": dummy_notify,
        "on_retry_callback": dummy_notify,
        **kwargs,
    }
