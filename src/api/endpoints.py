from fastapi import APIRouter

from src.api.routes.project import router as project_router


router = APIRouter()

router.include_router(router=project_router)
# router.include_router()
