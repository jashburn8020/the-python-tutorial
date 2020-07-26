"""Use configuration from a file as a `dictConfig`."""
import json
import logging
import logging.config
from pathlib import Path

config_path = Path(__file__).parent.joinpath("logging_config.json")
with open(config_path) as config_file:
    logging.config.dictConfig(json.load(config_file))

logger = logging.getLogger("logging_test.dictconfig")
logger.info("The message")
logger.warning("The message")
