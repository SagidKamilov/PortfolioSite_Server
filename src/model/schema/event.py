from pydantic import BaseModel


class EventCreate(BaseModel):
    title: str
    description: str


class EventUpdate(BaseModel):
    title: str | None
    description: str | None


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
