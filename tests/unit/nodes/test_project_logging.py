import logging
from logging import Logger

logger = logging.getLogger(__name__)


def test_default_logging(test_logging: None) -> None:
    logger.info("Base logger obtained successfully")

    assert isinstance(logger, Logger)
