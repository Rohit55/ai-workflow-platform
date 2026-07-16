"""
Organization API Routes.
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from app.database.session import get_db

from app.modules.organization.dependencies import (
    get_organization_service,
)

from app.modules.organization.schemas import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationUpdate
)

from app.modules.organization.service import (
    OrganizationService,
)

from app.core.responses import ApiResponse

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

    return ApiResponse.success(
        message="Organization created successfully.",
        data=jsonable_encoder(
            OrganizationResponse.model_validate(
                organization
            )
        ),
        status_code=201,
    )


@router.get("", response_model=list[OrganizationResponse],)
async def list_organization(
    db: AsyncSession = Depends(get_db),
    service: OrganizationService = Depends(get_organization_service)
):
    organization = await service.list(db)
    return ApiResponse.success(
        message="Organization list",
        data=jsonable_encoder([
            OrganizationResponse.model_validate(org)
            for org in organization
        ]),
        status_code=200,
    )
    # return [
    #     OrganizationResponse.model_validate(org)
    #     for org in organization
    # ]


@router.get(
    '/{organization_id}',
    response_model=OrganizationResponse
)
async def get_organization(
    organization_id: str,
    db: AsyncSession = Depends(get_db),
    service: OrganizationService = Depends(get_organization_service)
):
    organization = await service.get_by_id(db, organization_id)
    return ApiResponse.success(
        message="Organization data",
        data=jsonable_encoder(
            OrganizationResponse.model_validate(
                organization
            )
        ),
        status_code=200,
    )
    # return OrganizationResponse.model_validate(
    #     organization
    # )


@router.put(
    '/{organization_id}',
    response_model=OrganizationResponse,
)
async def update_organization(
    organization_id: str,
    payload: OrganizationUpdate,
    db: AsyncSession = Depends(get_db),
    service: OrganizationService = Depends(get_organization_service),
):
    organization = await service.update(db, organization_id, payload)
    return ApiResponse.success(
        message="Organization updated",
        data=jsonable_encoder(
            OrganizationResponse.model_validate(
                organization
            )
        ),
        status_code=200,
    )
    # return OrganizationResponse.model_validate(organization)
