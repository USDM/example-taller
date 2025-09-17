from ...use_cases.dto import WindowIndicatorType
from ...use_cases.generate_content_use_case.interfaces import ValidateUserInterface

class ValidateUserFree(ValidateUserInterface):
    def validate_user_with_indicator(self, indicator_type:WindowIndicatorType) -> WindowIndicatorType:
        if indicator_type.value == "sma":
            return WindowIndicatorType.SMA
        return None

        