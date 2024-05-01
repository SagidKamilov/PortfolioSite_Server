from typing import List

import sqlalchemy

from src.repository.base import BaseRepository
from src.model.db.form import Form
from src.model.schema.form import FormCreate, FormUpdate, FormResponse


class FormRepository(BaseRepository):
    async def create_form(self, form_create: FormCreate) -> Form:
        form = Form(
            email=form_create.email,
            title=form_create.title,
            description=form_create.description
        )

        self.session.add(form)
        await self.session.commit()

        return form

    async def get_form_by_id(self, form_id: int) -> Form | None:
        stmt = sqlalchemy.select(Form).where(Form.id == form_id)
        form = await self.session.execute(stmt)
        form = form.scalar()

        if not form:
            return None

        return form

    async def get_all_forms(self) -> List[Form]:
        stmt = sqlalchemy.select(Form)
        forms = await self.session.execute(stmt)
        forms = forms.scalars()
        forms = [
            form for form in forms
        ]

        return forms

    async def update_form_by_id(self, form_id: int, form_update: FormUpdate) -> Form | None:
        stmt = sqlalchemy.select(Form).where(Form.id == form_id)
        form = await self.session.execute(stmt)
        form = form.scalar()

        if not form:
            return None

        if form_update.email:
            form.email = form_update.email
        if form_update.title:
            form.title = form_update.title
        if form_update.description:
            form.description = form_update.description

        await self.session.commit()

        return form

    async def delete_form_by_id(self, form_id: int) -> str | None:
        stmt = sqlalchemy.select(Form).where(Form.id == form_id)
        form = await self.session.execute(stmt)
        form = form.scalar()

        if not form:
            return None

        stmt = sqlalchemy.delete(Form).where(Form.id == form_id)
        await self.session.execute(stmt)

        return f"Форма с id = `{form_id}` успешно удалена!"
