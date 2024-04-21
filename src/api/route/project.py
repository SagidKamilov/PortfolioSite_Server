from typing import List, Annotated

from fastapi import APIRouter, File, UploadFile, Form

from src.api.dependency.service_container import get_project_service
from src.model.schema.project import ProjectCreate, ProjectResponse, Photos


router = APIRouter(prefix="/project")


@router.post(path="")
async def create_project(main_photo: UploadFile,
                         additional_photo: UploadFile,
                         description_photo: List[UploadFile],
                         title: str = Form(...),
                         description: str = Form(...)):

    project = await get_project_service().create_project_with_photos(
        project_create=ProjectCreate(
            title=title,
            description=description
        ),
        main_photo=main_photo.file,
        additional_photo=additional_photo.file,
        description_photos=[description_photo_elem.file for description_photo_elem in description_photo]
    )
    return ProjectResponse(
        id=project.id,
        title=project.title,
        desctiption=project.description,
        main_photo=project.project_pictures.
    ) # Переделать таблицу хранения картинок для проекта. Хранить все фотографии со связью один к одному.
    # В одной записи картинки должны быть 3-8 картинки
