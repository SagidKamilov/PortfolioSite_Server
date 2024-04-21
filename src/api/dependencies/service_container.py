from typing import Callable, Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.repository.account import AccountRepository
from src.repository.project import ProjectRepository
from src.service.account import AccountService
from src.service.project_photo import DataControlService
from src.service.project import ProjectService
from src.service.photo import PhotoService
# from src.repository.settings import AsyncDatabase
from src.repository.settings import async_session


def account_service():
    account_repo = AccountRepository(async_session=async_session())
    return AccountService(account_repo=account_repo)


def get_project_service():
    project_repo = ProjectRepository(async_session=async_session())
    project_service = ProjectService(project_repo=project_repo)
    photo_service = PhotoService()
    project_photo_service = DataControlService(project_service=project_service, photo_service=photo_service)
    return project_photo_service
