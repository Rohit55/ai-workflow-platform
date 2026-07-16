import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import get_logger
from app.core.request_context import request_id_ctx

logger = get_logger(__name__)


class RequestContextMiddleware(
    BaseHTTPMiddleware,
):

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        request_id = str(uuid.uuid4())

        request_id_ctx.set(request_id)

        start = time.perf_counter()

        response = await call_next(request)

        duration = (
            time.perf_counter() - start
        ) * 1000

        logger.info(
            "HTTP Request",
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            status=response.status_code,
            duration_ms=round(duration, 2),
        )

        response.headers["X-Request-ID"] = request_id

        return response
