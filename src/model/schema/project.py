from typing import List

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    description: str


class ProjectCreatePicture(BaseModel):
    title: str
    description: str
    main_picture: str
    additional_picture: str
    description_pictures: List[str]


class ProjectUpdate(BaseModel):
    title: str
    description: str


class ProjectUpdatePictures(BaseModel):
    title: str | None
    description: str | None
    main_picture: str
    additional_picture: str
    description_pictures: List[str]


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    main_picture: str
    additional_picture: str
    description_pictures: List[str]
