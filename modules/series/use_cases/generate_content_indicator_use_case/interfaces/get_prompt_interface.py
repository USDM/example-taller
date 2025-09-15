from typing import Protocol
from ...dto import LastSerieDataInfo, WindowIndicatorType

class GetPromptInterface(Protocol):
    def get_prompt(self, last_serie_data:LastSerieDataInfo, indicators_info:list[WindowIndicatorType]) -> str:
        pass
