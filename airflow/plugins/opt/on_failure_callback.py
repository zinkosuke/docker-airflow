from logging import getLogger
from pprint import pformat

logger = getLogger(__name__)


def dummy_notify(*args, **kwargs):
    logger.info("on_failure_callback")
    logger.info(pformat(args))
    logger.info(pformat(kwargs))
