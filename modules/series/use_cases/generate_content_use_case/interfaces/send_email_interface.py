from typing import Protocol
from ...dto import User

class SendEmailInterface(Protocol):
    def send_email(self, user:User) -> str:
        pass