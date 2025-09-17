from ...use_cases.dto import UserData, UserType
from ...use_cases.generate_content_use_case.interfaces import LastSerieDataInterface, FactoryLastSerie
from . import (
    LastSerieDataFree,
    LastSerieDataPremium,
    LastSerieDataStudent,
    LastSerieDataSuscribed
)

class FactoryLastSerie(FactoryLastSerie):
    def create_last_serie(self, user_type: UserData) -> LastSerieDataInterface:
        if user_type.user_type == UserType.PREMIUM.value:
            return LastSerieDataPremium()
        elif user_type.user_type == UserType.FREE.value:
            return LastSerieDataFree()
        elif user_type.user_type == UserType.STUDENT.value:
            return LastSerieDataStudent()
        elif user_type.user_type == UserType.SUSCRIBED.value:
            return LastSerieDataSuscribed()