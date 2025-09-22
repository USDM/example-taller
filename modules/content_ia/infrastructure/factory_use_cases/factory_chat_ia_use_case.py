from ...use_cases.chat_ia_use_case.chat_ia_use_case import ChatIAUseCase
from ...search_content_repository.memory_search_content_repository import MemorySearchContentRepository
from ..save_response_ia_repo.memory_save_response_ia_repo import MemorySaveResponseIaRepo
from ..ia import GeminiIA
from ..user_repository import FactoryUserRepository
from ..factory_chat_ia import CreateFactoryChatIA
from ..factory_send_prompt import FactoryCreateSendPrompt
    
def create_chat_ia_use_case():
    search_content_repository = MemorySearchContentRepository()
    ia = GeminiIA()
    memory_save = MemorySaveResponseIaRepo()
    factory_user_repository = FactoryUserRepository()
    factory_send_message = CreateFactoryChatIA()
    factory_send_prompt = FactoryCreateSendPrompt()
    return ChatIAUseCase(search_content_repository, ia, memory_save, factory_user_repository, factory_send_message, factory_send_prompt)