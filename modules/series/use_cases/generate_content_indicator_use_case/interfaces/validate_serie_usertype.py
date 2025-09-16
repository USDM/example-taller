from typing import Protocol
from ...dto import UserType

class ValidateSerieUserTypeInterface(Protocol):
    def validate_user_type(self, serie_id:int, user_type:UserType) -> bool:
        pass