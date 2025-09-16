from typing import Protocol
from ...dto import UserType

class SendEmailInterface(Protocol):
    def send_email(self, user_type:UserType) -> str:
        pass