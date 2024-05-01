from typing import List

from src.repository.event import EventRepository
from src.model.schema.event import EventCreate, EventUpdate, EventResponse


class EventService:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    async def create_event(self, event_create: EventCreate) -> EventResponse:
        event = await self.event_repo.create_event(event_create)

        return EventResponse(
            id=event.id,
            title=event.title,
            description=event.description
        )

    async def get_event(self, event_id: int) -> EventResponse:
        event = await self.event_repo.get_event_by_id(event_id=event_id)

        if not event:
            raise Exception(f"События с id = `{event_id}` не существует!")

        return EventResponse(
            id=event.id,
            title=event.title,
            description=event.description
        )

    async def get_events(self) -> List[EventResponse]:
        events = await self.event_repo.get_all_events()

        events_response = [
            EventResponse(
                id=event.id,
                title=event.title,
                description=event.description
            )
            for event
            in events
        ]

        return events_response

    async def update_event(self, event_id: int, event_update: EventUpdate) -> EventResponse:
        event = await self.event_repo.update_form_by_id(event_id=event_id, event_update=event_update)

        if not event:
            raise Exception(f"Ошибка обновления! Формы с id = {event_id} не существует!")

        return EventResponse(
            id=event.id,
            title=event.title,
            description=event.description
        )

    async def delete_event(self, event_id: int) -> str:
        result = await self.event_repo.delete_event_by_id(event_id=event_id)

        if not result:
            raise Exception(f"Ошибка удаления! Формы с id={event_id} не существует!")

        return result
