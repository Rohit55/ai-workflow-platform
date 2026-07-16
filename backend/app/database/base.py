from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    """
    Base class for all database models.
    """

    pass


class BaseModel(Base):
    """
    Base model inherited by every table.
    """

    __abstract__ = True

    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid4())
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
