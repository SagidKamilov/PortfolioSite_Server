import datetime
from typing import List

import sqlalchemy
from sqlalchemy.sql import functions
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.db.base import Base
# from src.model.db.many_to_many import project_tag


class Project(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(name="title", type_=sqlalchemy.String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.Text, nullable=False)
    main_picture: Mapped[str] = mapped_column(name="main_picture", type_=sqlalchemy.Text, nullable=False)
    additional_picture: Mapped[str] = mapped_column(name="additional_picture", type_=sqlalchemy.Text, nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(name="create_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         nullable=False, server_default=functions.now())
    update_at: Mapped[datetime.datetime] = mapped_column(name="update_at", type_=sqlalchemy.DateTime(timezone=True),
                                                         server_default=functions.now())
    account_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey("account.id"))
    account: Mapped["Account"] = relationship(back_populates="projects")
    project_pictures: Mapped[List["Picture"]] = relationship(back_populates="project")
    # tags: Mapped[List["Tag"]] = relationship(secondary=project_tag, back_populates="projects")
