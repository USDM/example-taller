from ..use_cases.dto import UserType
from ..use_cases.chat_ia_use_case.interfaces.search_content_repository import SearchContentRepository
from ..use_cases.chat_ia_use_case.interfaces.factory_user_comments import FactoryUserComments
from .memory_search_content_free import MemorySearchContentFree
from .memory_search_content_repository import MemorySearchContentRepository
from .memory_search_content_suscribed import MemorySearchContentSuscribed

class FactoryUserComments(FactoryUserComments):
    def create_user_comments(self, user_type: UserType) -> SearchContentRepository:
        if user_type.value == UserType.PREMIUM.value or user_type.value== UserType.STUDENT.value:
            return MemorySearchContentRepository()
        elif user_type.value == UserType.FREE.value:
            return MemorySearchContentFree()
        elif user_type.value == UserType.SUSCRIBED.value:
            return MemorySearchContentSuscribed()
        else:
            raise("Tipo se usuario no soportado")