import datetime

from pydantic import BaseModel


class AccountCreate(BaseModel):
    username: str
    password: str
    role: str


class AccountUpdate(BaseModel):
    username: str | None
    password: str | None
    role: str | None


class AccountLogin(BaseModel):
    username: str
    password: str


class AccountResponse(BaseModel):
    id: int
    username: str
    role: str
