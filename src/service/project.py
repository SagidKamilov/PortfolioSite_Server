from typing import List

from src.repository.project import ProjectRepository
from src.model.db.project import Project
from src.model.schemas.project import ProjectCreatePhotos, ProjectUpdatePhotos, Photos
from src.exceptions.database import EntityDoesNotExist


class ProjectService:
    def __init__(self, project_repo: ProjectRepository):
        self.project_repo = project_repo

    async def create_project(self, project_create: ProjectCreatePhotos) -> Project:
        project = await self.project_repo.create_project(project_create=project_create)
        return project

    async def get_project(self, project_id: int) -> Project:
        project = await self.project_repo.get_project_by_id(project_id=project_id)
        if not project:
            raise EntityDoesNotExist(f"Проект с id = `{project_id} не найден`")
        return project

    async def get_all_projects(self) -> List[Project]:
        projects = await self.project_repo.get_all_projects()
        return projects

    async def update_project(self, project_id: int, project_update: ProjectUpdatePhotos) -> Project:
        project = await self.project_repo.update_project(project_id=project_id, project_update=project_update)
        return project

    async def delete_project(self, project_id: int):
        result: str = await self.project_repo.delete_project(project_id=project_id)
        return result
