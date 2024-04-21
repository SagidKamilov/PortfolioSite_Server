from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.api.endpoints import router
from src.config import settings

# app = FastAPI(prefix=settings.API_PREFIX)
app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     # allow_origins=[settings.ALLOWED_ORIGINS],
#     allow_origin=["*"],
#     # allow_credentials=[settings.IS_ALLOWED_CREDENTIALS],
#     allow_credentials=True,
#     # allow_methods=[settings.ALLOWED_METHODS],
#     allow_methods=["*"],
#     # allow_headers=[settings.ALLOWED_HEADERS],
#     allow_headers=["*"]
# )

app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        # host=settings.SERVER_HOST,
        # port=settings.SERVER_PORT,
        # workers=settings.SERVER_WORKERS,
        # log_level=settings.LOGGING_LEVEL,
    )