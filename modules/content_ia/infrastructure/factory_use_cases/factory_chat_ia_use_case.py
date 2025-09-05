from ..chat_ia_repository import ChatIARepository, SearchContentRepository
from ...use_cases.chat_ia_use_case.chat_ia_use_case import ChatIAUseCase
from ..ia import GeminiIA

def create_chat_ia_use_case(message: str, content_id: int) -> str:
    chat_ia_use_case = ChatIAUseCase(
        search_content_ia=SearchContentRepository(),
        base_ia=ChatIARepository(GeminiIA())
    )
    return chat_ia_use_case.chat_ia(content_id, message)