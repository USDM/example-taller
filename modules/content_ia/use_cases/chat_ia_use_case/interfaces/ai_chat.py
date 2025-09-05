from modules.content_ia.use_cases.dto import Content
from typing import Protocol


class AIChat(Protocol):

    def chat(self, message: str, content: Content) -> str:
        pass