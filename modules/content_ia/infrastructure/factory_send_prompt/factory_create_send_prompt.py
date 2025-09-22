from modules.content_ia.use_cases.chat_ia_use_case.interfaces.i_send_prompt import ISendPrompt
from .free_send_prompt import FreeSendPrompt
from .premium_send_prompt import PremiumSendPrompt
from .suscribed_send_prompt import SuscribedSendPrompt
from .student_send_prompt import StudentSendPrompt
from modules.content_ia.use_cases.dto import UserType


class FactoryCreateSendPrompt(ISendPrompt):
    def create(self, user_type: UserType) -> ISendPrompt:
        if user_type.value == UserType.FREE.value:
            return FreeSendPrompt()
        elif user_type.value == UserType.PREMIUM.value:
            return PremiumSendPrompt()
        elif user_type.value == UserType.SUSCRIBED.value:
            return SuscribedSendPrompt()
        elif user_type.value == UserType.STUDENT.value:
            return StudentSendPrompt()
        else:
            raise ValueError(f"User type {user_type} not supported")
