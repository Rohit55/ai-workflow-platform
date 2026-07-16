"""
Organization database model.
"""

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import BaseModel
from app.modules.organization.constants import OrganizationStatus


class Organization(BaseModel):
    """
    Organization entity.

    Every company/business using the platform
    is represented as an Organization.
    """

    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True,
        index=True,
    )

    slug: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default=OrganizationStatus.ACTIVE,
        nullable=False,
    )
