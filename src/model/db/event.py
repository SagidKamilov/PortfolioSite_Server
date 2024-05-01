from typing import List

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.db.base import Base
# from src.model.db.many_to_many import event_tag


class Event(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(name="title", type_=sqlalchemy.String(255), nullable=False)
    description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.Text, nullable=False)
    account_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey("account.id"))
    account: Mapped["Account"] = relationship(back_populates="events")
    # tags: Mapped[List["Tag"]] = relationship(secondary=event_tag, back_populates="events")
