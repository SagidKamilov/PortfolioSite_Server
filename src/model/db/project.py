import datetime
from typing import List

import sqlalchemy
from sqlalchemy.sql import functions
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.db.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(name="title", type_=sqlalchemy.String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.Text, nullable=False)
    main_picture: Mapped[str] = mapped_column(name="main_picture", type_=sqlalchemy.Text, nullable=False)
    additional_picture: Mapped[str] = mapped_column(name="additional_picture", type_=sqlalchemy.Text, nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(name="create_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         nullable=False, server_default=functions.now())
    update_at: Mapped[datetime.datetime] = mapped_column(name="update_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         server_default=functions.now())
    # account_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey("accounts.id"))
    # account: Mapped["Account"] = relationship(back_populates="project")
    project_pictures: Mapped[List["ProjectPicture"]] = relationship(back_populates="project")
