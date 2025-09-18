from ...use_cases.chat_ia_use_case.chat_ia_use_case import ChatIAUseCase
from ..user_repository import MemoryUserRepository
from ...search_content_repository import FactoryUserComments
from ..resume_comments_repository import FactoryResumeComments

def create_chat_ia_comments_use_case():
    user_repository = MemoryUserRepository()
    factory_user_comments = FactoryUserComments()
    factory_resume_comments = FactoryResumeComments()
    return ChatIAUseCase(
        search_user_repository=user_repository,
        factory_user_comments=factory_user_comments,
        factory_resume_comments=factory_resume_comments
    )