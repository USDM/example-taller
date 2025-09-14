from typing import Protocol
from ...dto import UserData

class SendEmailInterface(Protocol):
    def send_email_to_users(self, users:list[UserData]):
        pass