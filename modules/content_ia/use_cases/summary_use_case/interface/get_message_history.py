from typing import Protocol

class GetMessageHistoryInterface(Protocol):
    def get_message_history(self) -> list[dict]:
        pass