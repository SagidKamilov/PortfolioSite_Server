
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column

from src.model.db.base import Base


class Form(Base):
    __tablename__ = "form"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(name="email", type_=sqlalchemy.String(255), nullable=False)
    title: Mapped[str] = mapped_column(name="title", type_=sqlalchemy.String(255), nullable=False)
    description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.Text, nullable=False)
