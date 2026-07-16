"""
Business logic for Organizations.
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.organization.models import Organization
from app.modules.organization.schemas import (
    OrganizationCreate,
)

from app.shared.utils.slug import generate_slug
from app.modules.organization.exception import OrganizationAlreadyExistsException


class OrganizationService:

    async def create(
        self,
        db: AsyncSession,
        payload: OrganizationCreate,
    ) -> Organization:

        slug = generate_slug(payload.name)

        stmt = select(Organization).where(
            Organization.slug == slug
        )

        result = await db.execute(stmt)

        existing = result.scalar_one_or_none()

        if existing:
            raise OrganizationAlreadyExistsException()

        organization = Organization(

            name=payload.name,

            slug=slug,
        )

        db.add(organization)

        await db.commit()

        await db.refresh(organization)

        return organization
