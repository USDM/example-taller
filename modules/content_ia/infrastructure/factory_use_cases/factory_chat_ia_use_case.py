from ..search_content.search_content_repository import SearchContentRepository
from ..ai_chat.ai_chat_repository import AiChatRepository
from ...use_cases.chat_ia_use_case.chat_ia_use_case import ChatIAUseCase

def create_chat_ia_use_case():
    search_content = SearchContentRepository()
    ai_chat = AiChatRepository()
    return ChatIAUseCase(search_content, ai_chat)