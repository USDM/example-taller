from typing import Protocol
from ...dto import LastSerieDataInfo, WindowIndicatorType, ContentIndicatorInfo


class IGenerateContentIndicatorIA(Protocol):
    def generate_content_indicator_ia(self, prompt:str) -> ContentIndicatorInfo:
        pass