from ...dto import UserData
from typing import Protocol

class SearchUsersInterface(Protocol):
    def get_users(self) -> list[UserData]:
        pass