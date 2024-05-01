from typing import List

import sqlalchemy

from src.repository.base import BaseRepository
from src.model.db.account import Account
from src.model.schema.account import AccountCreate, AccountLogin, AccountUpdate


class AccountRepository(BaseRepository):
    async def create_account(self, account_create: AccountCreate) -> Account:
        new_account = Account(username=account_create.username, hash_password=account_create.password, role=account_create.role)
        self.session.add(instance=new_account)
        await self.session.commit()

        return new_account

    async def get_all_accounts(self) -> List[Account]:
        stmt = sqlalchemy.select(Account)
        accounts = await self.session.execute(statement=stmt)
        accounts = accounts.scalars()

        accounts = [
            account for account in accounts
        ]

        return accounts

    async def get_account_by_id(self, account_id: int) -> Account | None:
        stmt = sqlalchemy.select(Account).where(Account.id == account_id)
        account = await self.session.execute(statement=stmt)
        account = account.scalar()

        if not account:
            return None

        return account

    async def get_account_by_username(self, username: str) -> Account:
        stmt = sqlalchemy.select(Account).where(Account.username == username)
        account = await self.session.execute(statement=stmt)
        account = account.scalar()

        if not account:
            raise Exception(f"Аккаунт с именем пользователя = `{username}` не существует!")

        return account

    async def get_user_by_password(self, account_login: AccountLogin) -> Account | None:
        stmt = sqlalchemy.select(Account).where(Account.username == account_login.username)
        account = await self.session.execute(statement=stmt)
        account = account.scalar()

        if not account:
            return None

        if account_login.password != account.hash_password:
            return None

        return account

    async def update_account_by_id(self, account_id: int, account_update: AccountUpdate) -> Account | None:
        select_stmt = sqlalchemy.select(Account).where(Account.id == account_id)
        account = await self.session.execute(statement=select_stmt)
        account = account.scalar()

        if not account:
            return None

        if account_update.username:
            account.username = account_update.username

        if account_update.role:
            account.role = account_update.role

        if account_update.password:
            account.hash_password = account_update.password

        await self.session.commit()
        return account

    async def delete_account_by_id(self, account_id: int) -> str | None:
        select_stmt = sqlalchemy.select(Account).where(Account.id == account_id)
        query = await self.session.execute(statement=select_stmt)
        account = query.scalar()

        if not account:
            return None

        stmt = sqlalchemy.delete(table=Account).where(Account.id == account.id)

        await self.session.execute(statement=stmt)
        await self.session.commit()

        return f"Аккаунт с id = '{account_id}' был успешно удален!"

    async def check_username(self, username) -> Account | None:
        stmt = sqlalchemy.select(Account).where(Account.username == username)
        account = await self.session.execute(stmt)
        account = account.scalar()

        if not account:
            return None

        return account
