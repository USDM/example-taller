from typing import Protocol
from modules.content_ia.use_cases.dto import UserType

class GetPromptInterface(Protocol):
    def get_prompt(self, comments: list[str], question: str) -> str:
        pass