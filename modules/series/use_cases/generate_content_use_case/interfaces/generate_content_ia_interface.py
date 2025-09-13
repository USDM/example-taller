from typing import Protocol
from ...dto import ContentSerie
from ...dto import LastSerieDataInfo, WindowIndicatorData, WindowIndicatorType

class GenerateContentIAInterface(Protocol):
    def generate_content(self, serie_info:LastSerieDataInfo) -> ContentSerie:
        pass

    def generate_content_with_indicator(self, serie_info:LastSerieDataInfo, last_indicator_data: WindowIndicatorData, type_indicator: WindowIndicatorType) -> ContentSerie:
        pass