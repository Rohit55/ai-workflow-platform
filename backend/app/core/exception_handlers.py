import traceback

from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.exceptions import AppException
from app.core.logging import get_logger
from app.core.request_context import request_id_ctx

logger = get_logger(__name__)


async def app_exception_handler(
    request: Request,
    exc: AppException,
):

    logger.warning(
        "Application Exception",
        request_id=request_id_ctx.get(),
        path=request.url.path,
        error=exc.detail,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "code": exc.__class__.__name__.upper(),
        },
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):

    logger.warning(
        "Validation Error",
        request_id=request_id_ctx.get(),
        errors=exc.errors(),
    )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Failed",
            "code": "VALIDATION_ERROR",
            "errors": exc.errors(),
        },
    )


async def global_exception_handler(
    request: Request,
    exc: Exception,
):

    logger.exception(
        "Unhandled Exception",
        request_id=request_id_ctx.get(),
        path=request.url.path,
        traceback=traceback.format_exc(),
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "code": "INTERNAL_SERVER_ERROR",
        },
    )


def register_exception_handlers(
    app: FastAPI,
):

    app.add_exception_handler(
        AppException,
        app_exception_handler,
    )

    app.add_exception_handler(
        RequestValidationError,
        validation_exception_handler,
    )

    app.add_exception_handler(
        Exception,
        global_exception_handler,
    )
