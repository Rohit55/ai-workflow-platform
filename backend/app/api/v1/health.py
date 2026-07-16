from fastapi import APIRouter

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.database.session import get_db
from app.core.logging import get_logger


logger = get_logger(__name__)
router = APIRouter()


@router.get('/health')
async def health():
    logger.info(
        'Application Health check',
        module='Health'
    )

    return {
        'Status': 'Healthy'
    }


@router.get("/db-health")
async def db_health(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        text("SELECT 1")
    )

    return {
        "database": result.scalar()
    }
