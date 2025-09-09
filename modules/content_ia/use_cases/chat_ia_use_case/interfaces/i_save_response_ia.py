from typing import Protocol
class ISaveResponseIa(Protocol):
    def save_response(self, message):
        pass