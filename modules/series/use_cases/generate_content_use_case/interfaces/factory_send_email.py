from typing import Protocol
from ...dto import UserData
from .send_email_interface import SendEmailInterface

class FactorySendEmail(Protocol):
    def create_send_email(self, user_type: UserData) -> SendEmailInterface:
        pass