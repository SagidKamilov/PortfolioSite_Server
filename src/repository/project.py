from typing import Sequence, List, Tuple

import sqlalchemy
from sqlalchemy.sql import functions

from src.repository.base import BaseRepository
from src.model.db.project import Project
from src.model.db.picture import Picture
from src.model.schema.project import ProjectCreatePicture, ProjectUpdate


class ProjectRepository(BaseRepository):
    async def create_project(self, project_create: ProjectCreatePicture) -> Tuple[Project, Sequence[Picture]]:
        new_project = Project(title=project_create.title,
                              description=project_create.description,
                              main_picture=project_create.main_picture,
                              additional_picture=project_create.additional_picture,
                              account_id=project_create.account_id)
        self.session.add(new_project)
        await self.session.flush()

        for photo in project_create.description_pictures:
            description_photo = Picture(src_link=photo, project_id=new_project.id)
            self.session.add(description_photo)

        await self.session.commit()
        await self.session.refresh(instance=new_project)

        pictures = await self.get_picture_by_project_id(project_id=new_project.id)
        return new_project, pictures

    async def get_all_projects(self) -> Sequence[Project]:
        stmt = sqlalchemy.select(Project)
        all_projects = await self.session.execute(stmt)
        all_projects = all_projects.scalars().all()
        return all_projects

    async def get_project_by_id(self, project_id: int) -> Project | None:
        stmt = sqlalchemy.select(Project).where(Project.id == project_id)
        project = await self.session.execute(stmt)
        project = project.scalar()

        if not project:
            return None

        return project

    async def get_project_with_pictures(self, project_id: int) -> Tuple[Project, Sequence[Picture]] | None:
        project = self.get_project_by_id(project_id=project_id)
        pictures = await self.get_picture_by_project_id(project_id=project_id)

        return project, pictures

    async def get_picture_by_project_id(self, project_id: int) -> Sequence[Picture]:
        stmt = sqlalchemy.select(Picture.src_link).where(Picture.project_id == project_id)
        pictures = await self.session.execute(stmt)
        pictures = pictures.scalars().all()
        return pictures

    async def update_project_by_id(self, project_id: int, project_update: ProjectUpdate) -> Tuple[Project, Sequence[Picture]] | None:
        stmt = sqlalchemy.select(Project).where(Project.id == project_id)
        current_project = await self.session.execute(stmt)
        current_project = current_project.scalar()

        if not current_project:
            return None

        current_project.update_at = functions.now()
        if project_update.title:
            current_project.title = project_update.title
        if project_update.description:
            current_project.description = project_update.description

        await self.session.commit()

        pictures = self.get_picture_by_project_id(project_id=project_id)

        return current_project, pictures

    async def update_photo_by_project_id(self, project_id: int, main_picture: str = None, additional_picture: str = None,
                                         description_picture: str = None) -> str | None:
        project = self.get_project_by_id(project_id=project_id)

        if not project:
            return None

        message: str = ""

        if main_picture:
            message = main_picture
            project.main_picture = main_picture

        if additional_picture:
            message = additional_picture
            # stmt = sqlalchemy.update(Project.additional_picture).where(Project.id == project_id).values(
            #     additional_picture=additional_picture)
            # await self.session.execute(stmt)
            project.additional_picture = additional_picture

        if description_picture:
            message = description_picture
            stmt = sqlalchemy.update(Picture).where(Picture.project_id == project_id).values(src_link=description_picture)
            await self.session.execute(stmt)

        await self.session.commit()

        return f"Картинка с названием {message} успешно обновлена!"

    async def delete_photo_by_project_id(self, project_id: int, main_picture: str = None, additional_picture: str = None,
                                         description_picture: str = None) -> str | None:
        project = self.get_project_by_id(project_id=project_id)

        if not project:
            return None

        message: str = ""

        if main_picture:
            message = main_picture
            # stmt = sqlalchemy.delete(Project.main_picture).where(Project.id == project_id).where(
            #     Project.main_picture == main_picture)
            # await self.session.execute(stmt)
            project.main_picture = None

        if additional_picture:
            message = additional_picture
            # stmt = sqlalchemy.delete(Project.additional_picture).where(Project.id == project_id).where(
            #     Project.additional_picture == additional_picture)
            # await self.session.execute(stmt)
            project.additional_picture = None

        if description_picture:
            message = description_picture
            stmt = sqlalchemy.delete(Picture).where(Picture.project_id == project_id)
            await self.session.execute(stmt)

        await self.session.commit()

        return f"Картинка с названием {message} успешно удалена!"

    async def delete_project_by_id(self, project_id: int) -> str | None:
        stmt = sqlalchemy.select(Project).where(Project.id == project_id)
        project = await self.session.execute(stmt)
        project = project.scalar()

        if not project:
            return None

        stmt = sqlalchemy.delete(Project).where(Project.id == project_id)
        await self.session.execute(stmt)
        await self.session.commit()
        await self.session.close()

        return f"Проект с id = {project_id} успешно удален!"
