from ...use_cases.generate_content_use_case.interfaces import SendEmailInterface
from ...use_cases.dto import User, UserType

class SendEmail(SendEmailInterface):
    def send_email(self, user:User) -> str:
        if user.user_type.value == UserType.FREE.value:
            return(f"Cannot send email to {user.user_type.value}")
        else:
            return(f"Sending email to {user.email}, type {user.user_type.value}")