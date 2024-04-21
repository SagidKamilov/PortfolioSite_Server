import datetime
from typing import List

import sqlalchemy
from sqlalchemy.sql import functions
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.db.base import Base


class Project(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(name="title", type_=sqlalchemy.String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.Text, nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(name="create_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         nullable=False, server_default=functions.now())
    update_at: Mapped[datetime.datetime] = mapped_column(name="update_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         server_default=functions.now())
    # project_pictures: Mapped[List["ProjectPicture"]] = relationship(back_populates="projects")
