from typing import Protocol
from modules.content_ia.use_cases.dto import ContentComment

"""
    Objetivo: Enviar prompt a la IA
    Solo va a cambiar cuando la lógica de envío de prompt a la IA cambie
"""
class ChatIARepository(Protocol):
    def send_prompt(self, question: str, comments: list[ContentComment]) -> str:
        pass