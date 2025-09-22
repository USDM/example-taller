from typing import Protocol
from ...dto import ChatContent
from ...shared.base_ia import IA

class IGenerateSummary(Protocol):
    def generate_summary(self, chat_content: ChatContent, ia: IA) -> str:
        pass


