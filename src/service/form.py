from typing import List

from src.model.schema.form import FormCreate, FormResponse, FormUpdate
from src.repository.form import FormRepository


class FormService:
    def __init__(self, form_repo: FormRepository):
        self.form_repo = form_repo

    async def create_form(self, form_create: FormCreate) -> FormResponse:
        form = await self.form_repo.create_form(form_create=form_create)
        return FormResponse(
            id=form.id,
            email=form.email,
            title=form.title,
            description=form.description
        )

    async def get_form(self, form_id: int) -> FormResponse:
        form = await self.form_repo.get_form_by_id(form_id=form_id)

        if not form:
            raise Exception(f"Форма с id={form_id} не найдена!")

        return FormResponse(
            id=form.id,
            email=form.email,
            title=form.title,
            description=form.description
        )

    async def get_forms(self) -> List[FormResponse]:
        forms = await self.form_repo.get_all_forms()

        forms_response = [
            FormResponse(
                id=form.id,
                email=form.email,
                title=form.title,
                description=form.description
            )
            for form
            in forms
        ]

        return forms_response

    async def update_form(self, form_id, form_update: FormUpdate) -> FormResponse:
        form = await self.form_repo.update_form_by_id(form_id=form_id, form_update=form_update)

        if not form:
            raise Exception(f"Ошибка обновления! Формы с id={form_id} не существует!")

        return FormResponse(
            id=form.id,
            email=form.email,
            title=form.title,
            description=form.description
        )

    async def delete_form(self, form_id: int) -> str:
        result: str = await self.form_repo.delete_form_by_id(form_id=form_id)

        if not result:
            raise Exception(f"Ошибка удаления! Формы с id={form_id} не существует!")

        return result
