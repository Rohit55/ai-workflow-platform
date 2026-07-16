import logging
import sys

import structlog

from app.core.config import settings
from app.core.request_context import request_id_ctx


def configure_logging() -> None:
    """
    Configure application logging.
    """

    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    if settings.debug:
        processors.append(
            structlog.dev.ConsoleRenderer()
        )
    else:
        processors.append(
            structlog.processors.JSONRenderer()
        )

    structlog.configure(

        processors=processors,

        logger_factory=structlog.stdlib.LoggerFactory(),

        wrapper_class=structlog.stdlib.BoundLogger,

        cache_logger_on_first_use=True,
    )

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=settings.log_level,
    )


def get_logger(name: str):
    return structlog.get_logger(name)
