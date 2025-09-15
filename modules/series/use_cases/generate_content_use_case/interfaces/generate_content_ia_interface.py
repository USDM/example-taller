from typing import Protocol
from ...dto import ContentSerie
from ...dto import LastSerieDataInfo
from ...dto import WindowIndicatorType

class GenerateContentIAInterface(Protocol):
    def generate_content(self, serie_info:LastSerieDataInfo, indicators_info:list[WindowIndicatorType]) -> ContentSerie:
        pass