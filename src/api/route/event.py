from typing import List

from fastapi import APIRouter, status, HTTPException

from src.api.dependency.service_container import get_event_service
from src.model.schema.event import EventCreate, EventUpdate, EventResponse


router = APIRouter(prefix="/events", tags=["Действия над событиями"])


@router.post(path="", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
async def create_event(event_create: EventCreate):
    event = await get_event_service().create_event(event_create=event_create)

    return event


@router.get(path="/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
async def get_event(event_id: int):
    try:
        event = await get_event_service().get_event(event_id=event_id)

        return event
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.get(path="", response_model=List[EventResponse], status_code=status.HTTP_200_OK)
async def get_events():
    events = await get_event_service().get_events()

    return events


@router.put(path="/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
async def update_event(event_id: int, event_update: EventUpdate):
    try:
        event = await get_event_service().update_event(event_id=event_id, event_update=event_update)

        return event
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.delete(path="/{event_id}", response_model=str, status_code=status.HTTP_200_OK)
async def delete_event(event_id: int):
    try:
        result = await get_event_service().delete_event(event_id=event_id)

        return result
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

