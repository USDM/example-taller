from ...use_cases.chat_ia_use_case.chat_ia_use_case import ChatIAUseCase
from ..search_content_repository import MemorySearchContentRepository
from ..ia import GeminiIA

def create_chat_ia_use_case():
    ia = GeminiIA()
    search_content_repository = MemorySearchContentRepository()
    return ChatIAUseCase(search_content_repository, ia)