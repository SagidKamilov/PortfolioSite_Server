import datetime
from typing import List

import sqlalchemy
from sqlalchemy.sql import functions
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.db.base import Base
from src.model.db.project_picture import ProjectPicture


class Project(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(name="title", type=sqlalchemy.String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(name="description", type=sqlalchemy.Text, nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(name="create_at", type=sqlalchemy.DateTime(timezone=True),
                                                         nullable=False, server_default=functions.now())
    update_at: Mapped[datetime.datetime] = mapped_column(name="create_at", type=sqlalchemy.DateTime(timezone=True),
                                                         nullable=False, server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True))
    project_pictures: Mapped[List["ProjectPicture"]] = relationship(back_populates="project")
