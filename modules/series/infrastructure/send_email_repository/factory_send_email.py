from ...use_cases.dto import UserData, UserType
from ...use_cases.generate_content_use_case.interfaces import FactorySendEmail, SendEmailInterface
from . import (
    SendEmailFree,
    SendEmailPremium,
    SendEmailStudent,
    SendEmailSuscribed
)

class FactorySendEmail(FactorySendEmail):
    def create_send_email(self, user_type: UserData) -> SendEmailInterface:
        if user_type.user_type == UserType.PREMIUM.value:
            return SendEmailPremium()
        elif user_type.user_type == UserType.FREE.value:
            return SendEmailFree()
        elif user_type.user_type == UserType.STUDENT.value:
            return SendEmailStudent()
        elif user_type.user_type == UserType.SUSCRIBED.value:
            return SendEmailSuscribed()