from app.core.exceptions import ConflictException, NotFoundException


class OrganizationAlreadyExistsException(ConflictException):
    def __init__(self):
        super().__init__("Organization already exists.")


class OrganizationNameEmptyException(NotFoundException):
    def __init__(self):
        super().__init__("Organization name cannot be empty")
