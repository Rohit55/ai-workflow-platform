"""
Application configuration.

This file is the SINGLE SOURCE OF TRUTH
for all application configuration.

Never call os.getenv() anywhere else.

Author: Rohit
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.
    Values are automatically loaded
    from .env
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    # ---------------------------------------------------
    # Application
    # ---------------------------------------------------

    app_name: str = "AI Workforce Platform"

    app_env: str = "development"

    app_host: str = "0.0.0.0"

    app_port: int = 8000

    debug: bool = True

    project_version: str

    api_prefix: str

    log_level: str = "INFO"

    # ---------------------------------------------------
    # Database
    # ---------------------------------------------------

    database_url: str

    # ---------------------------------------------------
    # Redis
    # ---------------------------------------------------

    redis_host: str

    redis_port: int

    # ---------------------------------------------------
    # JWT
    # ---------------------------------------------------

    jwt_secret: str

    jwt_algorithm: str = "HS256"

    jwt_expire_minutes: int = 60

    # ---------------------------------------------------
    # OpenAI
    # ---------------------------------------------------

    openai_api_key: str | None = None

    # ---------------------------------------------------
    # MinIO
    # ---------------------------------------------------

    minio_endpoint: str

    minio_root_user: str

    minio_root_password: str

    minio_bucket: str


@lru_cache
def get_settings() -> Settings:
    """
    Creates ONE Settings object.
    Singleton Pattern.
    """
    return Settings()


settings = get_settings()
