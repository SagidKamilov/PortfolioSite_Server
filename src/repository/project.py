from typing import Sequence, List

import sqlalchemy
from sqlalchemy.sql import functions

from src.repository.base import BaseRepository
from src.model.db.project import Project
from src.model.db.project_picture import ProjectPicture
from src.model.schema.project import ProjectCreatePhotos, ProjectUpdatePhotos, Photos
from src.exception.database import EntityDoesNotExist, EntityAlreadyExists


class ProjectRepository(BaseRepository):
    async def create_project(self, project_create: ProjectCreatePhotos) -> Project:
        new_project = Project(title=project_create.title, description=project_create.description)
        self.session.add(new_project)
        await self.session.flush()

        main_photo = ProjectPicture(name_photo=project_create.photos.main_photo, type_picture="main", project_id=new_project.id)
        self.session.add(main_photo)
        additional_photo = ProjectPicture(name_photo=project_create.photos.additional_photo, type_picture="additional", project_id=new_project.id)
        self.session.add(additional_photo)
        for photo in project_create.photos.description_photos:
            description_photo = ProjectPicture(name_photo=photo, type_picture="description", project_id=new_project.id)
            self.session.add(description_photo)

        await self.session.commit()
        await self.session.refresh(instance=new_project)
        return new_project

    async def get_all_projects(self) -> Sequence[Project]:
        stmt = sqlalchemy.select(Project)
        all_projects = await self.session.execute(stmt)
        return all_projects.scalars().all()

    async def get_project_by_id(self, project_id: int) -> Project | None:
        stmt = sqlalchemy.select(Project).where(Project.id == project_id)
        project = await self.session.execute(stmt)

        if not project:
            return None

        return project.scalar()

    async def update_project(self, project_id: int, project_update: ProjectUpdatePhotos) -> Project:
        stmt = sqlalchemy.select(Project).where(Project.id == project_id)
        current_project = await self.session.execute(stmt)

        if not current_project:
            raise EntityDoesNotExist(f"Ошибка обновления! Проекта с id = `{project_id}` не существует!")

        stmt = sqlalchemy.update(Project).where(Project.id == project_id).values(update_at=functions.now())
        if project_update.title:
            stmt = stmt.values(title=project_update.title)
        if project_update.description:
            stmt = stmt.values(desciption=project_update.description)
        if project_update.photos.main_photo:
            stmt = stmt.values()

    async def delete_project(self, project_id: int) -> str:
        stmt = sqlalchemy.select(Project).where(Project.id == project_id)
        current_project = self.session.execute(stmt)

        if not current_project:
            raise EntityDoesNotExist(f"Ошибка удаления! Проекта с id = `{project_id}` не существует!")

        stmt = sqlalchemy.delete(Project).where(Project.id == project_id)
        await self.session.execute(stmt)
        await self.session.commit()

        return f"Проект с id = {project_id} успешно удален!"
