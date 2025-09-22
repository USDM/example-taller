from ..get_summary.factory_get_summary import FactoryGetSummary
from ..get_message_history.get_message_history_repo import GetMessageHistoryRepo
from ...use_cases.summary_use_case.summary_use_case import SummaryUseCase
from ..ia import GeminiIA

def create_summary_use_case():
    ia = GeminiIA()
    get_summary_factory = FactoryGetSummary()
    get_message_history = GetMessageHistoryRepo()
    return SummaryUseCase(ia, get_summary_factory, get_message_history)