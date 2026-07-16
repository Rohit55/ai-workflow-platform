from typing import Any

from fastapi.responses import JSONResponse


class ApiResponse:

    @staticmethod
    def success(
        data: Any = None,
        message: str = "Success",
        status_code: int = 200,
    ):

        return JSONResponse(
            status_code=status_code,
            content={
                "success": True,
                "message": message,
                "data": data,
            },
        )

    @staticmethod
    def error(
        message: str,
        code: str,
        status_code: int,
        errors: list | None = None,
    ):

        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "message": message,
                "code": code,
                "errors": errors,
            },
        )
