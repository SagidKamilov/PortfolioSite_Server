from typing import List

from src.security.password import HashGenerator
from src.repository.account import AccountRepository
from src.model.schema.account import AccountCreate, AccountUpdate, AccountResponse, AccountLogin


class AccountService:
    def __init__(self, account_repo: AccountRepository):
        self.hash_generator = HashGenerator()
        self.account_repo = account_repo

    async def create_account(self, account_create: AccountCreate) -> AccountResponse:
        if await self.account_repo.check_username(username=account_create.username):
            raise Exception(f"Имя `{account_create.username}` уже занято!")

        hashed_password: str = self.hash_generator.generate_hash_from_password(password=account_create.password)
        account = await self.account_repo.create_account(account_create=AccountCreate(
            username=account_create.username,
            role=account_create.role,
            password=hashed_password
        ))

        return AccountResponse(
            id=account.id,
            username=account.username,
            role=account.role
        )

    async def check_login(self, account_login: AccountLogin) -> AccountResponse:
        hashed_password: str = self.hash_generator.generate_hash_from_password(password=account_login.password)

        hash_account_login = AccountLogin(
            username=account_login.username,
            password=hashed_password
        )

        account = await self.account_repo.get_user_by_password(account_login=hash_account_login)

        if not account:
            raise Exception(f"Пароли не совпадают!")

        return AccountResponse(
            id=account.id,
            username=account.username,
            role=account.username
        )

    async def get_accounts(self) -> List[AccountResponse]:
        accounts = await self.account_repo.get_all_accounts()

        accounts_response = [
            AccountResponse(
                id=account.id,
                username=account.username,
                role=account.role
            )
            for account
            in accounts
        ]

        return accounts_response

    async def get_account(self, account_id: int) -> AccountResponse:
        account = await self.account_repo.get_account_by_id(account_id=account_id)

        if not account:
            raise Exception(f"Аккаунт с id = `{account_id}` не существует!")

        return AccountResponse(
            id=account.id,
            username=account.username,
            role=account.role,
            password=account.hash_password
        )

    async def update_account(self, account_id: int, account_update: AccountUpdate) -> AccountResponse:
        account = await self.account_repo.update_account_by_id(account_id=account_id, account_update=account_update)

        if not account:
            raise Exception(f"Ошибка обновления! Аккаунт с id = `{account_id}` не существует!")

        return AccountResponse(
            id=account.id,
            username=account.username,
            role=account.role
        )

    async def delete_account(self, account_id: int) -> str:
        result: str = await self.account_repo.delete_account_by_id(account_id=account_id)

        if not result:
            raise Exception(f"Ошибка удаления! Аккаунт с id = `{account_id}` не был найден!")

        return result
