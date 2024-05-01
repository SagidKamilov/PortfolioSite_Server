from typing import List, Annotated

from fastapi import APIRouter, File, UploadFile, Form, status, HTTPException

from src.api.dependency.service_container import get_project_service
from src.model.schema.project import ProjectCreate, ProjectUpdate, ProjectResponse


router = APIRouter(prefix="/projects", tags=["Действия над проектом"])


@router.post(path="", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(main_picture: UploadFile,
                         additional_picture: UploadFile,
                         description_pictures: List[UploadFile],
                         project_create: ProjectCreate):

    project_response = await get_project_service().create_project_with_photos(
        project_create=project_create,
        main_picture=main_picture.file,
        additional_picture=additional_picture.file,
        description_pictures=[
            description_photo_elem.file for description_photo_elem in description_pictures
        ]
    )

    return project_response


@router.get(path="/{project_id}", response_model=ProjectResponse, status_code=status.HTTP_200_OK)
async def get_project(project_id: int):
    try:
        project_response = await get_project_service().get_project_with_pictures(project_id=project_id)
        return project_response
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.get(path="", response_model=List[ProjectResponse], status_code=status.HTTP_200_OK)
async def get_projects():
    project_response = await get_project_service().get_projects()
    return project_response


@router.put(path="/{project_id}", response_model=ProjectResponse, status_code=status.HTTP_200_OK)
async def update_project(project_id: int, title: str = Form(...), description: str = Form(...)):
    try:
        project_response = await get_project_service().update_project(
            project_id=project_id,
            project_update=ProjectUpdate(
                title=title,
                description=description
            )
        )

        return project_response
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.put(path="/{project_id}/picture", response_model=str, status_code=status.HTTP_200_OK)
async def update_picture(project_id: int, type_picture: str, picture: UploadFile):
    try:
        result: str = ""

        if type_picture == "main":
            result = await get_project_service().update_picture(project_id=project_id, main_picture=picture)
        elif type_picture == "additional":
            result = await get_project_service().update_picture(project_id=project_id, additional_picture=picture)
        elif type_picture == "description":
            result = await get_project_service().update_picture(project_id=project_id, description_picture=picture)

        return result
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.delete(path="/{project_id}/picture", response_model=str, status_code=status.HTTP_200_OK)
async def delete_picture(project_id: int, type_picture: str, picture: UploadFile):
    try:
        result: str = ""

        if type_picture == "main":
            result = await get_project_service().delete_picture(project_id=project_id, main_picture=picture)
        elif type_picture == "additional":
            result = await get_project_service().delete_picture(project_id=project_id, additional_picture=picture)
        elif type_picture == "description":
            result = await get_project_service().delete_picture(project_id=project_id, description_picture=picture)

        return result
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.delete(path="/{project_id}", status_code=status.HTTP_200_OK)
async def delete_project(project_id: int):
    try:
        result_message = await get_project_service().delete_project_by_id(project_id=project_id)
        return result_message
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
