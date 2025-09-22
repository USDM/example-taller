from typing import Protocol
from ...use_cases.chat_ia_use_case.interfaces import ValidateTotalMessagesInterface
from modules.common.tables import TableResponseIa
from modules.content_ia.use_cases.dto import UserType

class ValidateTotalMessages(ValidateTotalMessagesInterface):
    def validate_total_messages(self, user_type: UserType) -> bool:
        memory_messages = TableResponseIa().data

        new_message = {
            UserType.FREE.value: lambda: len(memory_messages) < 5,
            UserType.SUSCRIBED.value: lambda: len(memory_messages) < 100,
            UserType.PREMIUM.value: lambda: True,
            UserType.STUDENT.value: lambda: True
        }

        return new_message[user_type.value]()