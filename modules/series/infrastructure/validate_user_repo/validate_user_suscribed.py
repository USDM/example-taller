from ...use_cases.dto import WindowIndicatorType
from ...use_cases.generate_content_use_case.interfaces import ValidateUserInterface

class ValidateUserSuscribed(ValidateUserInterface):
    def validate_user_with_indicator(self, indicator_type:WindowIndicatorType) -> WindowIndicatorType:
        if indicator_type.value == "sma":
            return WindowIndicatorType.SMA
        elif indicator_type.value == "roc":
            return WindowIndicatorType.ROC
        elif indicator_type.value == "rsi":
            return WindowIndicatorType.RSI
        return None