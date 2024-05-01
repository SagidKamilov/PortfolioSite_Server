from typing import Callable, Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.repository.account import AccountRepository
from src.repository.project import ProjectRepository
from src.repository.form import FormRepository
from src.repository.event import EventRepository

from src.service.account import AccountService
from src.service.project_picture import DataControlService
from src.service.project import ProjectService
from src.service.picture import PictureService
from src.service.form import FormService
from src.service.event import EventService
# from src.repository.settings import AsyncDatabase
from src.repository.settings import AsyncDatabase


async_database = AsyncDatabase()
async_database.initialize_engine()
async_database.initialize_session()

async_session = async_database.get_session()


def get_account_service():
    account_repo = AccountRepository(async_session=async_session())
    account_service = AccountService(account_repo=account_repo)
    return account_service


def get_project_service():
    project_repo = ProjectRepository(async_session=async_session())
    project_service = ProjectService(project_repo=project_repo)
    photo_service = PictureService()
    project_photo_service = DataControlService(project_service=project_service, picture_service=photo_service)
    return project_photo_service


def get_form_service():
    form_repo = FormRepository(async_session=async_session())
    form_service = FormService(form_repo=form_repo)
    return form_service


def get_event_service():
    event_repo = EventRepository(async_session=async_session())
    event_service = EventService(event_repo=event_repo)
    return event_service
