"""
Business logic for Organizations.
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.organization.models import Organization
from app.modules.organization.schemas import (
    OrganizationCreate,
    OrganizationUpdate,
)

from app.shared.utils.slug import generate_slug
from app.modules.organization.exception import OrganizationAlreadyExistsException, OrganizationNameNotFoundException


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

    async def _get_by_slug(
        self,
        db: AsyncSession,
        slug: str,
    ) -> Organization | None:
        pass

    async def get_by_id(
            self,
            db: AsyncSession,
            organization_id: str,
    ) -> Organization:
        stmt = select(Organization).where(
            Organization.id == organization_id
        )
        result = await db.execute(stmt)
        organization = result.scalar_one_or_none()
        if organization is None:
            raise OrganizationNameNotFoundException
        return organization

    async def list(
        self,
        db: AsyncSession,
    ) -> list[Organization]:
        stmt = select(Organization).order_by(
            Organization.created_at.desc()
        )
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_by_name(
            self,
            db: AsyncSession,
            name: str,
    ) -> Organization:

        stmt = select(Organization).where(
            Organization.name == name
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def update(
            self,
            db: AsyncSession,
            organization_id: str,
            payload: OrganizationUpdate,
    ) -> Organization:

        organization = await self.get_by_id(db, organization_id)
        if payload.name is not None:
            existing = await self.get_by_name(db, payload.name)
            if (existing and existing.id != organization.id):
                raise OrganizationAlreadyExistsException
            organization.name = payload.name
        await db.commit()
        await db.refresh(organization)
        return organization
