from fastapi import APIRouter, status, Depends, HTTPException

from src.api.dependency.service_container import get_account_service
from src.model.schema.account import AccountResponse, AccountCreate, AccountLogin


router = APIRouter(prefix="/auth", tags=["Аутентификация пользователей"])


@router.post(path="/signup", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def sign_up(account_create: AccountCreate):
    try:
        account = await get_account_service().create_account(account_create=account_create)

        return account
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.post(path="/signin", response_model=AccountResponse, status_code=status.HTTP_202_ACCEPTED)
async def sign_in(account_login: AccountLogin):
    try:
        account = await get_account_service().check_login(account_login=account_login)

        return account
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(error))
