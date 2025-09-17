from ...use_cases.dto import UserData, UserType
from ...use_cases.generate_content_use_case.interfaces import FactoryValidateUser, ValidateUserInterface
from . import (
    ValidateUserFree,
    ValidateUserPremium, 
    ValidateUserStudent,
    ValidateUserSuscribed
)

class FactoryValidateUser(FactoryValidateUser):
    def create_calculate_indicator(self, user_type: UserData) -> ValidateUserInterface:
        if user_type.user_type == UserType.PREMIUM.value:
            return ValidateUserPremium()
        elif user_type.user_type == UserType.FREE.value:
            return ValidateUserFree()
        elif user_type.user_type== UserType.STUDENT.value:
            return ValidateUserStudent()
        elif user_type.user_type == UserType.SUSCRIBED.value:
            return ValidateUserSuscribed()