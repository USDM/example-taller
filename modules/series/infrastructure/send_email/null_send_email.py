from ...use_cases.generate_content_indicator_use_case.interfaces import SendEmailInterface
from ...use_cases.dto import UserType

class NullSendEmail(SendEmailInterface):
    def send_email(self, user_type:UserType) -> str:
        return(f"Cannot send email to {user_type.value}")