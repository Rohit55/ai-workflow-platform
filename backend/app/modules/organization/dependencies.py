"""
Organization dependencies.
"""

from app.modules.organization.service import OrganizationService


def get_organization_service() -> OrganizationService:
    """
    Dependency Injection for OrganizationService.
    """
    return OrganizationService()
