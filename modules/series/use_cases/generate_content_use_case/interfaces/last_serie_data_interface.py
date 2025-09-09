from typing import Protocol
from ...dto import LastSerieDataInfo

class LastSerieDataInterface(Protocol):
    def get_last_data(self, serie_id:int) -> LastSerieDataInfo:
        pass