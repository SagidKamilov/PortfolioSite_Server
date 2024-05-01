from fastapi import APIRouter

from src.api.route.auth import router as auth_router
from src.api.route.account import router as account_router
from src.api.route.project import router as project_router
from src.api.route.event import router as event_router
from src.api.route.form import router as form_router


router = APIRouter()

router.include_router(router=auth_router)
router.include_router(router=account_router)
router.include_router(router=project_router)
router.include_router(router=event_router)
router.include_router(router=form_router)
