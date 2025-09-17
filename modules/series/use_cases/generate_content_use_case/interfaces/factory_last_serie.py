from ...dto import UserData
from typing import Protocol
from .last_serie_data_interface import LastSerieDataInterface

class FactoryLastSerie(Protocol):
    def create_last_serie(self, user_type: UserData) -> LastSerieDataInterface:
        pass