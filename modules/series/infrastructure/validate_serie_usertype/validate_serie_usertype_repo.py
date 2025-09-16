from ...use_cases.generate_content_indicator_use_case.interfaces import ValidateSerieUserTypeInterface
from modules.common.tables import TableSeriesMatch
from modules.series.use_cases.dto import UserType

class ValidateSerieUserType(ValidateSerieUserTypeInterface):
    def validate_user_type(self, serie_id:int, user_type:UserType) -> bool:
        series = TableSeriesMatch().data

        for serie in series.values():
            if serie.get("id") == serie_id:
                importance = serie.get("importance")
                break

        validator = {
            user_type.FREE.value: lambda: True if importance <= 1 else False,
            user_type.SUSCRIBED.value: lambda: True if importance <= 2 else False,
            user_type.STUDENT.value: lambda: True if importance <= 3 else False,
            user_type.PREMIUM.value: lambda: True if importance <= 4 else False,
        }

        return validator[user_type.value]()