# from sqlalchemy import Table, Column, ForeignKey
#
#
# from src.model.db.base import Base
#
#
# project_tag = Table(
#     "project_tag",
#     Base.metadata,
#     Column("project_id", ForeignKey("project.id"), primary_key=True),
#     Column("tag_id", ForeignKey("tag.id"), primary_key=True)
# )
#
# event_tag = Table(
#     "event_tag",
#     Base.metadata,
#     Column("tag_id", ForeignKey("tag.id"), primary_key=True),
#     Column("event_id", ForeignKey("event.id"), primary_key=True)
# )
#
