from typing import List, Sequence, Tuple

from src.repository.project import ProjectRepository
from src.model.db.project import Project
from src.model.db.picture import ProjectPicture
from src.model.schema.project import ProjectCreatePicture, ProjectUpdatePictures


class ProjectService:
    def __init__(self, project_repo: ProjectRepository):
        self.project_repo = project_repo

    async def create_project(self, project_create: ProjectCreatePicture) -> Tuple[Project, Sequence[ProjectPicture]]:
        project_pictures = await self.project_repo.create_project(project_create=project_create)
        return project_pictures

    async def get_project(self, project_id: int) -> Tuple[Project, Sequence[ProjectPicture]]:
        project_pictures = await self.project_repo.get_project_by_id(project_id=project_id)

        if not project_pictures:
            raise Exception(f"Проект с id = `{project_id} не найден`")

        return project_pictures

    async def get_all_projects(self) -> Sequence[Project]:
        projects = await self.project_repo.get_all_projects()
        return projects

    async def update_project(self, project_id: int, project_update: ProjectUpdatePictures) -> Project:
        project_pictures = await self.project_repo.update_project(project_id=project_id, project_update=project_update)

        if not project_pictures:
            raise Exception(f"Ошибка обновления! Проекта с id = `{project_id}` не существует!")

        return project_pictures

    async def delete_project(self, project_id: int) -> str:
        result: str = await self.project_repo.delete_project(project_id=project_id)

        if not result:
            raise Exception(f"Ошибка удаления! Проекта с id = `{project_id}` не существует!")

        return result
