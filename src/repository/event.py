from typing import List

import sqlalchemy

from src.repository.base import BaseRepository
from src.model.db.event import Event
from src.model.schema.event import EventCreate, EventUpdate


class EventRepository(BaseRepository):
    async def create_event(self, event_create: EventCreate) -> Event:
        event = Event(
            title=event_create.title,
            description=event_create.description
        )

        self.session.add(Event)
        await self.session.commit()

        return event

    async def get_event_by_id(self, event_id: int) -> Event | None:
        stmt = sqlalchemy.select(Event).where(Event.id == event_id)
        event = await self.session.execute(stmt)
        event = event.scalar()

        if not event:
            return None

        return event

    async def get_all_events(self) -> List[Event]:
        stmt = sqlalchemy.select(Event)
        events = await self.session.execute(stmt)
        events = events.scalars()
        events = [
            event for event in events
        ]

        return events

    async def update_form_by_id(self, event_id: int, event_update: EventUpdate) -> Event | None:
        stmt = sqlalchemy.select(Event).where(Event.id == event_id)
        event = await self.session.execute(stmt)
        event = event.scalar()

        if not event:
            return None

        if event_update.title:
            event.title = event_update.title
        if event_update.description:
            event.description = event_update.description

        await self.session.commit()

        return event

    async def delete_event_by_id(self, event_id: int) -> str | None:
        stmt = sqlalchemy.select(Event).where(Event.id == event_id)
        event = await self.session.execute(stmt)
        event = event.scalar()

        if not event:
            return None

        stmt = sqlalchemy.delete(Event).where(Event.id == event_id)
        await self.session.execute(stmt)

        return f"Событие с id = `{event_id}` успешно удалена!"
