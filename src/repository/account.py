from typing import Sequence

import sqlalchemy
from sqlalchemy.sql.functions import now

from src.repository.base import BaseRepository
from src.model.db.account import Account
from src.model.schemas.account import AccountCreate, AccountLogin, AccountUpdate
from src.exceptions.database import EntityDoesNotExist, EntityAlreadyExists, PasswordDoesNotMatch


class AccountRepository(BaseRepository):
    async def create_account(self, account_create: AccountCreate):
        new_account = Account(username=account_create.username, hash_password=account_create.password, role=account_create.role)
        self.session.add(instance=new_account)
        await self.session.commit()
        return new_account

    async def read_accounts(self) -> Sequence[Account]:
        stmt = sqlalchemy.select(Account)
        query = await self.session.execute(statement=stmt)
        return query.scalars().all()

    async def read_account_by_id(self, account_id: int) -> Account:
        stmt = sqlalchemy.select(Account).where(Account.id == account_id)
        query = await self.session.execute(statement=stmt)
        if not query:
            raise EntityDoesNotExist(f"Аккаунт с id = `{account_id}` не существует!")
        return query.scalar()

    async def read_account_by_username(self, username: str) -> Account:
        stmt = sqlalchemy.select(Account).where(Account.username == username)
        query = await self.session.execute(statement=stmt)
        if not query:
            raise EntityDoesNotExist(f"Аккаунт с именем пользователя = `{username}` не существует!")
        return query.scalar()

    async def read_user_by_password(self, account_login: AccountLogin) -> Account:
        stmt = sqlalchemy.select(Account).where(Account.username == account_login.username)
        query = await self.session.execute(statement=stmt)
        found_account = query.scalar()
        if not found_account:
            raise EntityDoesNotExist("Неправильное имя пользователя!")
        if found_account.password != account_login.password:
            raise PasswordDoesNotMatch("Неправильный пароль!")
        return found_account

    async def update_account_by_id(self, account_id: int, account_update: AccountUpdate) -> Account:
        select_stmt = sqlalchemy.select(Account).where(Account.id == account_id)
        query = await self.session.execute(statement=select_stmt)
        update_account = query.scalar()

        if not update_account:
            raise EntityDoesNotExist(f"Аккаунт с id = `{account_id}` не существует!")

        update_stmt = sqlalchemy.update(table=Account).where(Account.id == update_account.id).values(
            updated_at=now())

        if account_update.username:
            update_stmt = update_stmt.values(username=account_update.username)

        if account_update.role:
            update_stmt = update_stmt.values(role=account_update.role)

        if account_update.password:
            update_stmt = update_stmt.values(password=account_update.password)

        await self.session.execute(statement=update_stmt)
        await self.session.commit()
        return update_account

    async def delete_account_by_id(self, account_id: int) -> str:
        select_stmt = sqlalchemy.select(Account).where(Account.id == account_id)
        query = await self.session.execute(statement=select_stmt)
        delete_account = query.scalar()

        if not delete_account:
            raise EntityDoesNotExist(f"Аккаунт с id = `{account_id}` не был найден!")

        stmt = sqlalchemy.delete(table=Account).where(Account.id == delete_account.id)

        await self.session.execute(statement=stmt)
        await self.session.commit()

        return f"Аккаунт с id = '{account_id}' был успешно удален!"

    async def check_login(self, username):
        stmt = sqlalchemy.select(Account).where(Account.username == username)
        checked_account = await self.session.execute(stmt)

        if checked_account:
            raise EntityAlreadyExists(f"Имя `{username}` уже занято!")
