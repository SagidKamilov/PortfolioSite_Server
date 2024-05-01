# from typing import List
#
# import sqlalchemy
# from sqlalchemy.orm import Mapped, mapped_column, relationship
#
# from src.model.db.base import Base
# from src.model.db.many_to_many import event_tag, project_tag
#
#
# class Tag(Base):
#     __tablename__ = "tag"
#
#     id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(name="title", type_=sqlalchemy.String(50), nullable=False, unique=True)
#     description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.String(255), nullable=False)
#     events: Mapped[List["Event"]] = relationship(secondary=event_tag, back_populates="tags")
#     projects: Mapped[List["Project"]] = relationship(secondary=project_tag, back_populates="tags")
