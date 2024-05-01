from typing import List

from fastapi import APIRouter, status, Form, HTTPException

from src.api.dependency.service_container import get_form_service
from src.model.schema.form import FormCreate, FormResponse, FormUpdate

router = APIRouter(prefix="/forms", tags=["Действия над формой"])


@router.post(path="", response_model=FormResponse, status_code=status.HTTP_201_CREATED)
async def create_form(title: str = Form(...),
                      email: str = Form(...),
                      description: str = Form(...)):

    form = await get_form_service().create_form(
        form_create=FormCreate(
            email=email,
            title=title,
            description=description
        )
    )

    return form


@router.get(path="/{form_id}", response_model=FormResponse, status_code=status.HTTP_200_OK)
async def get_form(form_id: int):

    try:
        form = await get_form_service().get_form(form_id=form_id)

        return form
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.get(path="", response_model=List[FormResponse], status_code=status.HTTP_200_OK)
async def get_forms():

    forms = await get_form_service().get_forms()

    return forms


@router.put(path="/{form_id}", response_model=FormResponse, status_code=status.HTTP_200_OK)
async def update_form(form_id: int,
                      email: str | None = Form(...),
                      title: str | None = Form(...),
                      description: str | None = Form(...)):
    try:
        form = await get_form_service().update_form(
            form_id=form_id,
            form_update=FormUpdate(
                email=email,
                title=title,
                description=description
            )
        )

        return form
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.delete(path="/{form_id}", response_model=str, status_code=status.HTTP_200_OK)
async def delete_form(form_id: int):
    try:
        result = await get_form_service().delete_form(form_id=form_id)

        return result
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
