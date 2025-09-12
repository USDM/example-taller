from typing import Protocol
from ...dto import LastSerieDataInfo
from ...dto import WindowIndicatorType


class IGenerateContentIndicatorIA(Protocol):
    def generate_content_indicator_ia(self, last_serie_data:LastSerieDataInfo, indicators_info:list[WindowIndicatorType]) -> ContentIndicatorInfo:
        pass