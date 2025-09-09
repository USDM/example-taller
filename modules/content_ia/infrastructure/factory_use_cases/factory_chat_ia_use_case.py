from ...use_cases.chat_ia_use_case.chat_ia_use_case import ChatIAUseCase
from ...search_content_repository.memory_search_content_repository import MemorySearchContentRepository
from ..save_response_ia_repo.memory_save_response_ia_repo import MemorySaveResponseIaRepo
from ..ia import GeminiIA

def create_chat_ia_use_case():
    search_content_repository = MemorySearchContentRepository()
    ia = GeminiIA()
    memory_save = MemorySaveResponseIaRepo()
    return ChatIAUseCase(search_content_repository, ia, memory_save)