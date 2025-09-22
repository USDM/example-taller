from typing import Protocol
from modules.content_ia.use_cases.shared.base_ia import IA

class GetSummaryInterface(Protocol):
    def get_summary(self, ia: IA, history: list[dict]) -> str:
        pass