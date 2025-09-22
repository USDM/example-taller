from typing import Protocol
from modules.content_ia.use_cases.dto import PlanConfig

class ISendMessage(Protocol):
    def send_message(self, message: str, plan_config: PlanConfig, max_messages: int) -> str:
        pass