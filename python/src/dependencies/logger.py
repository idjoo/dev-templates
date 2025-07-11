import logging
import sys
from typing import Annotated

from fastapi import Depends
from google.cloud.logging.handlers import StructuredLogHandler

from src.dependencies import Config


async def init():
    config: Config = Config()

    logger = logging.getLogger(config.service)
    logger.setLevel(config.logging.level.upper())
    logger.addHandler(StructuredLogHandler(stream=sys.stdout))


async def get_logger(config: Config) -> logging.Logger:
    return logging.getLogger(config.service)


Logger = Annotated[logging.Logger, Depends(get_logger)]
