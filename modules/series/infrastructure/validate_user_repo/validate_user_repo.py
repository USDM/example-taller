from typing import Protocol
from ...use_cases.dto import UserData, WindowIndicatorType
from ...use_cases.generate_content_use_case.interfaces import ValidateUserInterface

class ValidateUserRepo(ValidateUserInterface):
    def validate_user_with_indicator(self, user_data:UserData, indicator:WindowIndicatorType) -> bool:
        if user_data.user_type in ["premium", "student"]:
            return True
        elif user_data.user_type == "free" and indicator.name == "SMA":
            return True
        elif user_data.user_type == "subscribed" and indicator.name in ["SMA", "ROC", "RSI"]:
            return True
        else:
            return False
