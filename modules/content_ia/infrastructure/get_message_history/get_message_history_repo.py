from modules.content_ia.use_cases.summary_use_case.interface.get_message_history import GetMessageHistoryInterface
from modules.common.tables import TableResponseIa

class GetMessageHistoryRepo(GetMessageHistoryInterface):
    def get_message_history(self) -> list[dict]:
        return TableResponseIa().data