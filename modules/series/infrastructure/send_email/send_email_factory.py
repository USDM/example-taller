from ...use_cases.generate_content_indicator_use_case.interfaces import SendEmailInterface
from ...use_cases.dto import UserType
from .send_email_repo import SendEmail
from .null_send_email import NullSendEmail

class SendEmailFactory:
    def create(self, user_type:UserType) -> SendEmailInterface:
        if user_type.value == UserType.FREE.value:
            return NullSendEmail()
        else:
            return SendEmail()