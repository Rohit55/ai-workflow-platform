"""
Pydantic schemas for the Organization module.

These schemas are responsible for:
1. Request validation
2. Response serialization
3. OpenAPI (Swagger) documentation
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator
from app.modules.organization.exception import OrganizationAlreadyExistsException, OrganizationNameEmptyException


class OrganizationBase(BaseModel):
    """
    Common fields shared across organization schemas.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=150,
        examples=["Apollo Clinic"],
        description="Organization name",
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """
        Trim whitespace and validate organization name.
        """

        value = value.strip()

        if not value:
            raise OrganizationAlreadyExistsException()

        return value


class OrganizationCreate(OrganizationBase):
    """
    Request body for creating a new organization.
    """

    pass


class OrganizationUpdate(BaseModel):
    """
    Request body for updating an organization.

    All fields are optional because a client
    may update only one field.
    """

    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=150,
        description="Updated organization name",
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """
        Validate updated organization name.
        """

        if value is None:
            return value

        value = value.strip()

        if not value:
            raise OrganizationNameEmptyException()

        return value


class OrganizationResponse(OrganizationBase):
    """
    Response returned to the client.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    slug: str

    status: str

    created_at: datetime

    updated_at: datetime
