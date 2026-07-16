from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging, get_logger
from app.api.v1.health import router as healthRouter

from app.modules.organization.api import (
    router as organization_router,
)

from app.core.exception_handlers import (
    register_exception_handlers,
)

from app.core.middleware import (
    RequestContextMiddleware,
)

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):

    configure_logging()

    logger.info(
        "Application Started",
        environment=settings.app_env,
    )

    yield

    logger.info(
        "Application Shutdown"
    )


app = FastAPI(

    title=settings.app_name,

    version=settings.project_version,

    lifespan=lifespan,

    debug=settings.debug,
)

app.add_middleware(
    RequestContextMiddleware,
)

register_exception_handlers(app)

app.include_router(healthRouter, prefix=settings.api_prefix)
app.include_router(organization_router, prefix=settings.api_prefix)


@app.get('/')
async def root():
    return {
        'Message': 'Server up and Runner'
    }
