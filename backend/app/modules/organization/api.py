"""
Organization API Routes.
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db

from app.modules.organization.dependencies import (
    get_organization_service,
)

from app.modules.organization.schemas import (
    OrganizationCreate,
    OrganizationResponse,
)

from app.modules.organization.service import (
    OrganizationService,
)

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "",
    response_model=OrganizationResponse,
    status_code=201,
)
async def create_organization(
    payload: OrganizationCreate,
    db: AsyncSession = Depends(get_db),
    service: OrganizationService = Depends(
        get_organization_service
    ),
):

    organization = await service.create(
        db=db,
        payload=payload,
    )

    return OrganizationResponse.model_validate(
        organization
    )
