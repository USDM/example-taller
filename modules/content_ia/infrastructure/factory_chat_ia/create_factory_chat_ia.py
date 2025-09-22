from modules.content_ia.use_cases.dto import UserType
from modules.content_ia.use_cases.chat_ia_use_case.interfaces.i_send_message import ISendMessage
from .free_factory_send_message import FreeFactorySendMessage
from .premium_factory_send_message import PremiumFactorySendMessage
from .suscribed_factory_send_message import SuscribedFactorySendMessage
from .student_factory_send_message import StudentFactorySendMessage

class CreateFactoryChatIA(ISendMessage):
    def create(self, user_type: UserType) -> ISendMessage:
        if user_type.value == UserType.FREE.value:
            return FreeFactorySendMessage()
        elif user_type.value == UserType.PREMIUM.value:
            return PremiumFactorySendMessage()
        elif user_type.value == UserType.SUSCRIBED.value:
            return SuscribedFactorySendMessage()
        elif user_type.value == UserType.STUDENT.value:
            return StudentFactorySendMessage()
        else:
            raise ValueError(f"User type {user_type} not supported")