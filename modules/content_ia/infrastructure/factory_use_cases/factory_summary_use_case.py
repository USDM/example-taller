from ...use_cases.summary_use_case.summary_use_case import SummaryUseCase
from ..user_repository import FactoryUserRepository
from ..factory_summary_chat import MemorySearchChatContent
from ..factory_summary_chat import PremiumGenerateSummary
from ..ia import GeminiIA


def create_summary_use_case():
    factory_user_repository = FactoryUserRepository()
    search_chat_content_repository = MemorySearchChatContent()
    generate_summary_repository = PremiumGenerateSummary()
    ia = GeminiIA()
    return SummaryUseCase(factory_user_repository, search_chat_content_repository, generate_summary_repository, ia)