import fastapi

from src.message.exceptions.http_details import http_401_unauthorized_details


async def http_exc_401_cunauthorized_request() -> Exception:
    return fastapi.HTTPException(
        status_code=fastapi.status.HTTP_400_BAD_REQUEST,
        detail=http_401_unauthorized_details(),
    )
