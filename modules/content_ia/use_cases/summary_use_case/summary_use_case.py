from modules.content_ia.use_cases.shared.base_ia import IA
from modules.content_ia.use_cases.dto import UserType
from modules.content_ia.infrastructure.get_summary.factory_get_summary import FactoryGetSummary
from modules.content_ia.use_cases.summary_use_case.interface.get_message_history import GetMessageHistoryInterface

class SummaryUseCase:
    def __init__(self, ia: IA, get_summary_factory: FactoryGetSummary, get_message_history: GetMessageHistoryInterface):
        self.get_summary_factory = get_summary_factory
        self.ia = ia
        self.get_message_history = get_message_history

    def generate_summary(self, user_type: UserType):
        """
        1. Recibir el tipo de usuario
        2. obtener el history de la conversacion
        3. obtener el resumen de la conversacion
        4. retornar el resumen

        1. None
        2. GetMessageHistoryInterface
        3. GetSummaryInterface
        4. None
        """
        history = self.get_message_history.get_message_history()
        get_summary_factory = self.get_summary_factory.create(user_type)
        response = get_summary_factory.get_summary(self.ia, history)

        return response, history