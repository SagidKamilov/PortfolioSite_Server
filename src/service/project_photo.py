from typing import List, Any

from src.model.db.project import Project
from src.service.project import ProjectService
from src.service.photo import PhotoService
from src.model.schemas.project import ProjectCreate, ProjectCreatePhotos, ProjectUpdate, ProjectUpdatePhotos, Photos


class DataControlService:
    def __init__(self, project_service: ProjectService, photo_service: PhotoService):
        self.project_service = project_service
        self.photo_service = photo_service

    async def create_project_with_photos(self, project_create: ProjectCreate,
                                         main_photo,
                                         additional_photo,
                                         description_photos: List[Any]) -> Project:

        name_main_photo = await self.photo_service.save_photo(new_photo=main_photo, type_photo="main_photo")
        name_additional_photo = await self.photo_service.save_photo(new_photo=additional_photo, type_photo="additional_photo")
        name_description_photos = []
        for photo in description_photos:
            name_description_photo = await self.photo_service.save_photo(new_photo=photo, type_photo="description_photo")
            name_description_photos.append(name_description_photo)

        project_create_photos = ProjectCreatePhotos(
            title=project_create.title,
            description=project_create.description,
            photos=Photos(
                main_photo=name_main_photo,
                additional_photo=name_additional_photo,
                description_photos=name_description_photos
            )
        )

        project = await self.project_service.create_project(project_create=project_create_photos)
        return project

    async def get_projects(self) -> List[Project]:
        projects = await self.project_service.get_all_projects()
        return projects

    async def get_project_by_id(self, project_id: int) -> Project:
        project = await self.project_service.get_project(project_id=project_id)
        return project

    async def update_project_by_id(self, project_id: int,
                                   project_update: ProjectUpdate,
                                   main_photo,
                                   additional_photo,
                                   description_photos: List[Any]) -> Project:

        new_name_main_photo = await self.photo_service.save_photo(new_photo=main_photo, type_photo="main_photo")
        new_name_additional_photo = await self.photo_service.save_photo(new_photo=additional_photo, type_photo="additional_photo")
        new_name_description_photos = []
        for photo in description_photos:
            name_description_photo = await self.photo_service.save_photo(new_photo=photo, type_photo="description_photo")
            new_name_description_photos.append(name_description_photo)

        project_update_photos = ProjectUpdatePhotos(
            title=project_update.title,
            description=project_update.description,
            photos=Photos(
                main_photo=new_name_main_photo,
                additional_photo=new_name_additional_photo,
                description_photos=new_name_description_photos
            )
        )

        project = await self.project_service.update_project(project_id=project_id, project_update=project_update_photos)
        return project

    async def delete_project_by_id(self, project_id: int) -> str:
        result: str = await self.project_service.delete_project(project_id=project_id)
        return result
