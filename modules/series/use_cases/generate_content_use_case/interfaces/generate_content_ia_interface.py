from typing import Protocol
from ...dto import ContentSerie
from ...dto import LastSerieDataInfo

class GenerateContentIAInterface(Protocol):
    def generate_content(self, serie_info:LastSerieDataInfo) -> ContentSerie:
        pass