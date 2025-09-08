from typing import Protocol
from ...dto import Content

class SendEmailRepository(Protocol):
    def send_email(self, email: str, contents: list[Content]):
        pass