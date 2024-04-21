import datetime

import sqlalchemy
from sqlalchemy.sql import functions
from sqlalchemy.orm import mapped_column, Mapped

from src.model.db.base import Base


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement="auto")
    username: Mapped[str] = mapped_column(name="username", type_=sqlalchemy.String(length=255), nullable=False, unique=True)
    hash_password: Mapped[str] = mapped_column(name="hash_password", type_=sqlalchemy.String, nullable=True)
    role: Mapped[str] = mapped_column(name="role", type_=sqlalchemy.String(length=255), nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(name="create_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         nullable=False, server_default=functions.now())
    update_at: Mapped[datetime.datetime] = mapped_column(name="update_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         nullable=False, server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True))
