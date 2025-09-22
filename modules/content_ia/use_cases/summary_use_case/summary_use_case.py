from ...use_cases.generate_content_use_case.interfaces import FactoryUserRepository
from ...use_cases.summary_use_case.interfaces import ISearchChatContentRepository
import os
from ...use_cases.dto import UserType
from ...use_cases.summary_use_case.interfaces import IGenerateSummary
from ...use_cases.shared.base_ia import IA

class SummaryUseCase:

    def __init__(self,
                factory_user_repository: FactoryUserRepository,
                search_chat_content_repository: ISearchChatContentRepository,
                generate_summary_repository: IGenerateSummary,
                ia: IA
                ):
        self.factory_user_repository = factory_user_repository
        self.search_chat_content_repository = search_chat_content_repository
        self.generate_summary_repository = generate_summary_repository
        self.ia = ia
    def get_summary(self, chat_content_id: int, user_id: int) -> str:
        """
        1.- Recibir el id del chat
        2.- Recibir el id del usuario
        3.- Obtener el contenido del chat
        4.- Generar el resumen
        5.- Retornar el resumen

        1.- None
        2.- None
        3.- SearchChatContentRepository
        4.- IGenerateSummaryIA
        5.- None
        """
        user_repository = self.factory_user_repository.create_using_mode(os.getenv("MODE"))
        user_type = user_repository.get_user_type(user_id)

        if user_type.value != UserType.PREMIUM.value:
            raise Exception("You are not a premium user, you can't generate a summary")

        chat_content = self.search_chat_content_repository.get_chat_content(chat_content_id)

        summary = self.generate_summary_repository.generate_summary(chat_content.chat_content_response, self.ia)

        print("summary", summary)
