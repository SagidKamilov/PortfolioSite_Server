from typing import List

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.db.base import Base
from src.model.db.project import Project


class ProjectPicture(Base):
    __tablename__ = "project_picture"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    src_link: Mapped[str] = mapped_column(name="src_link", type_=sqlalchemy.Text, nullable=False)
    type_picture: Mapped[str] = mapped_column(name="type_picture", type_=sqlalchemy.String(length=255))
    project_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey(Project.id, ondelete="CASCADE"))
    project: Mapped["Project"] = relationship(back_populates="project_picture")