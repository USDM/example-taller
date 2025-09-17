from typing import Protocol
from ...dto import UserData
from .validate_user_interface import ValidateUserInterface

class FactoryValidateUser(Protocol):
    def create_calculate_indicator(self, user_type: UserData) -> ValidateUserInterface:
        pass