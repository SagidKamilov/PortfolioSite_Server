from typing import List

from fastapi import APIRouter, status, Depends, HTTPException

from src.api.dependency.service_container import get_account_service
from src.model.schema.account import AccountResponse, AccountCreate, AccountLogin


router = APIRouter(prefix="/accounts", tags=["Действия над аккаунтами"])


@router.get(path="/{account_id}", response_model=AccountResponse, status_code=status.HTTP_200_OK)
async def get_account(account_id: int):
    try:
        account = await get_account_service().get_account(account_id=account_id)

        return account
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.get(path="", response_model=List[AccountResponse], status_code=status.HTTP_200_OK)
async def get_accounts():
    accounts = await get_account_service().get_accounts()

    return accounts


@router.put(path="/{account_id}", response_model=AccountResponse, status_code=status.HTTP_200_OK)
async def update_account(account_id: int):
    try:
        account = await get_account_service().update_account(account_id=account_id)

        return account
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.delete(path="/{account_id}", response_model=AccountResponse, status_code=status.HTTP_200_OK)
async def delete_account(account_id: int):
    try:
        result: str = await get_account_service().delete_account(account_id=account_id)

        return result
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
