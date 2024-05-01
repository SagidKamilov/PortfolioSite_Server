from typing import List, Any, Tuple, Sequence

from src.model.db.project import Project
from src.service.project import ProjectService
from src.service.picture import PictureService
from src.model.schema.project import ProjectCreate, ProjectCreatePicture, ProjectUpdate, ProjectResponse


class DataControlService:
    def __init__(self, project_service: ProjectService, picture_service: PictureService):
        self.project_service = project_service
        self.picture_service = picture_service

    async def create_project_with_photos(self, project_create: ProjectCreate,
                                         main_picture,
                                         additional_picture,
                                         description_pictures: List[Any]) -> ProjectResponse | None:
        try:
            name_main_picture = await self.picture_service.save_picture(type_picture="main_picture",
                                                                        new_picture=main_picture)

            name_additional_picture = await self.picture_service.save_picture(type_picture="additional_picture",
                                                                              new_picture=additional_picture)

            name_description_picture = [
                await self.picture_service.save_picture(type_picture="description_picture", new_picture=picture)
                for picture
                in description_pictures
            ]

            project_create_picture = ProjectCreatePicture(
                title=project_create.title,
                description=project_create.description,
                main_picture=name_main_picture,
                additional_picture=name_additional_picture,
                description_pictures=name_description_picture,
                account_id=project_create.account_id
            )

            project, pictures = await self.project_service.create_project(project_create=project_create_picture)

            project_response = ProjectResponse(
                id=project.id,
                title=project.title,
                description=project.description,
                main_picture=project.main_picture,
                additional_picture=project.additional_picture,
                description_pictures=pictures,
                account_id=project.account_id
            )

            return project_response
        except Exception as error:
            raise error

    async def get_projects(self) -> List[ProjectResponse]:
        projects = await self.project_service.get_all_projects()
        projects_response = [
            await self.get_project_by_id(project_id=project.id) for project in projects
        ]
        return projects_response

    async def get_project_by_id(self, project_id: int) -> ProjectResponse | None:
        try:
            project, pictures = await self.project_service.get_project(project_id=project_id)

            project_response = ProjectResponse(
                id=project.id,
                title=project.title,
                description=project.description,
                main_picture=project.main_picture,
                additional_picture=project.additional_picture,
                description_pictures=pictures
            )

            return project_response
        except Exception as error_entity:
            raise error_entity

    async def update_project(self, project_id: int, project_update: ProjectUpdate) -> ProjectResponse:
        try:
            project, pictures = await self.project_service.update_project(project_id=project_id,
                                                                          project_update=project_update)

            project_response = ProjectResponse(
                id=project.id,
                title=project.title,
                description=project.description,
                main_picture=project.main_picture,
                additional_picture=project.additional_picture,
                description_picture=pictures
            )

            return project_response
        except Exception as error_entity:
            raise error_entity

    async def update_picture(self, project_id: int, main_picture: bytes = None, additional_picture: bytes = None,
                             description_picture: bytes = None) -> str:
        try:
            result: str = ""

            if main_picture:
                picture_name = await self.picture_service.save_picture(type_picture="main_picture",
                                                                       new_picture=main_picture)
                result = await self.project_service.update_picture(project_id=project_id, main_picture=picture_name)
            if additional_picture:
                picture_name = await self.picture_service.save_picture(type_picture="additional_picture",
                                                                       new_picture=additional_picture)
                result = await self.project_service.update_picture(project_id=project_id,
                                                                   additional_picture=picture_name)
            if description_picture:
                picture_name = await self.picture_service.save_picture(type_picture="description_picture",
                                                                       new_picture=description_picture)
                result = await self.project_service.update_picture(project_id=project_id,
                                                                   description_picture=picture_name)

            return result
        except Exception as error_entity:
            raise error_entity

    async def delete_picture(self, project_id: int, main_picture: str | None, additional_picture: str | None,
                           description_picture: str | None) -> str:
        try:
            result: str = ""

            if main_picture:
                await self.picture_service.delete_picture(picture_name=main_picture)
                result = await self.project_service.delete_picture(project_id=project_id, main_picture=main_picture)

            if additional_picture:
                await self.picture_service.delete_picture(picture_name=additional_picture)
                result = await self.project_service.delete_picture(project_id=project_id,
                                                                   additional_picture=additional_picture)

            if description_picture:
                await self.picture_service.delete_picture(picture_name=description_picture)
                result = await self.project_service.delete_picture(project_id=project_id,
                                                                   description_picture=description_picture)

            return result
        except Exception as error_entity:
            raise error_entity

    async def delete_project_by_id(self, project_id: int) -> str | None:
        try:
            result: str = await self.project_service.delete_project(project_id=project_id)
            return result
        except Exception as error:
            raise error
