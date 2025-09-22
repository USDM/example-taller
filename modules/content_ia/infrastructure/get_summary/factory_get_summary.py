from modules.content_ia.use_cases.dto import UserType
from modules.content_ia.use_cases.summary_use_case.interface.get_summary import GetSummaryInterface
from .get_summary_repo import GetSummaryRepo
from .null_get_summary import NullGetSummary


class FactoryGetSummary:
    def create(self, user_type: UserType) -> GetSummaryInterface:
        if user_type.value == UserType.PREMIUM.value:
            return GetSummaryRepo()
        else:
            return NullGetSummary()