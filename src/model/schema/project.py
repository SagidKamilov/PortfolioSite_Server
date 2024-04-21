from typing import List

from pydantic import BaseModel


class Photos(BaseModel):
    main_photo: str
    additional_photo: str
    description_photos: List[str]


class ProjectCreate(BaseModel):
    title: str
    description: str


class ProjectCreatePhotos(BaseModel):
    title: str
    description: str
    photos: Photos


class ProjectUpdate(BaseModel):
    title: str
    description: str


class ProjectUpdatePhotos(BaseModel):
    title: str | None
    description: str | None
    photos: Photos


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    photos: Photos
