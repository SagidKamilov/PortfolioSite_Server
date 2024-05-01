from typing import List

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    description: str
    account_id: int


class ProjectCreatePicture(BaseModel):
    title: str
    description: str
    main_picture: str
    additional_picture: str
    description_pictures: List[str]
    account_id: int


class ProjectUpdate(BaseModel):
    title: str | None
    description: str | None


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    main_picture: str
    additional_picture: str
    description_pictures: List[str]
    account_id: int
