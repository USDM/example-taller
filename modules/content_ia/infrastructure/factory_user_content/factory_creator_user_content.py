from modules.content_ia.infrastructure.factory_chat_ia.free_factory_send_message import FreeFactorySendMessage
from modules.content_ia.infrastructure.factory_chat_ia.suscribed_factory_send_message import SuscribedFactorySendMessage
from modules.content_ia.infrastructure.factory_chat_ia.premium_factory_send_message import PremiumFactorySendMessage
from modules.content_ia.infrastructure.factory_chat_ia.student_factory_send_message import StudentFactorySendMessage
from modules.content_ia.use_cases.dto import UserType
from modules.content_ia.use_cases.generate_content_use_case.interfaces import FactoryUserContent
from modules.content_ia.use_cases.generate_content_use_case.interfaces import FactoryCreatorUserContent as FactoryCreatorUserContentInterface

class FactoryCreatorUserContent(FactoryCreatorUserContentInterface):

  def create(self, user_type:UserType) -> FactoryUserContent:
    if user_type.value == UserType.FREE.value:
        return FreeFactorySendMessage()
    elif user_type.value == UserType.SUSCRIBED.value:
        return SuscribedFactorySendMessage()
    elif user_type.value == UserType.PREMIUM.value:
        return PremiumFactorySendMessage()
    elif user_type.value == UserType.STUDENT.value:
        return StudentFactorySendMessage()
    else:
        raise ValueError(f"User type {user_type} not supported")