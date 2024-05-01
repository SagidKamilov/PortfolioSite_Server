from pydantic import BaseModel


class FormCreate(BaseModel):
    email: str
    title: str
    description: str


class FormUpdate(BaseModel):
    email: str | None
    title: str | None
    description: str | None


class FormResponse(BaseModel):
    id: int
    email: str
    title: str
    description: str
