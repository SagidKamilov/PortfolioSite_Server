from src.repository.account import AccountRepository
from src.model.schemas.account import AccountCreate


class AccountService:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    def create_account(self, account_create: AccountCreate):
        try:
            self.account_repo.create_account(account_create=account_create)
        except:
            raise
