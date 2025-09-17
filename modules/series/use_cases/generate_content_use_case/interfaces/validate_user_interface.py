from typing import Protocol
from ...dto import UserData, WindowIndicatorType

class ValidateUserInterface(Protocol):
    def validate_user_with_indicator(self, indicator_type:WindowIndicatorType) -> WindowIndicatorType:
        pass
