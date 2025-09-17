from typing import Protocol
from ...dto import UserData

class SendEmailInterface(Protocol):
    def send_email_to_user(self, user_data:UserData) -> str:
        pass