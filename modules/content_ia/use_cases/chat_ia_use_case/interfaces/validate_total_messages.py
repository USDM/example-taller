from typing import Protocol
from modules.content_ia.use_cases.dto import UserType

class ValidateTotalMessagesInterface(Protocol):
    def validate_total_messages(self, user_type: UserType) -> bool:
        pass