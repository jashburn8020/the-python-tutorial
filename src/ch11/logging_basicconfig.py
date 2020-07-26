"""Apply configuration using `basicConfig`."""
import logging
import logging.config
import sys

logging.basicConfig(
    stream=sys.stdout,
    style="{",
    datefmt="%d/%m/%Y %H:%M:%S",
    format="{asctime} {levelname:<8} {module} [{thread}]: {message}",
    level="DEBUG",
)

logger = logging.getLogger(__name__)
logger.info("The message")
logger.warning("The message")
