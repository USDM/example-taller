from typing import Protocol
from modules.content_ia.use_cases.shared.base_ia import IA

class ISendPrompt(Protocol):
    def send_prompt(self, comments: list[str], question: str, ia: IA) -> str:
        pass