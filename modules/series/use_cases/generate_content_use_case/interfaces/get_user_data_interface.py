from typing import Protocol
from ...dto import User

class GetUserDataInterface(Protocol):
    def get_user(self, user_id:int) -> User:
        pass