"""
Application Exception
"""
from fastapi import HTTPException
from starlette.status import *


class AppException(HTTPException):
    """
    Base Exception for application.
    """

    def __init__(
        self,
        status_code: int,
        detail: str,
    ):
        super().__init__(
            status_code=status_code,
            detail=detail,
        )


class NotFoundException(AppException):
    def __init__(self, detail="Resource not found"):
        super().__init__(
            status_code=404,
            detail=detail
        )


class ConflictException(AppException):
    def __init__(self, detail="Conflict"):
        super().__init__(status_code=409, detail=detail)


class ValidationException(AppException):
    def __init__(self, detail="Validation Error"):
        super().__init__(status_code=400, detail=detail)


class UnauthorizedException(AppException):
    def __init__(self, detail="Unauthorized"):
        super().__init__(status_code=401, detail=detail)


class ForbiddenException(AppException):
    def __int__(self):
        super().__init__(status_code=403, detail="Forbidden")
