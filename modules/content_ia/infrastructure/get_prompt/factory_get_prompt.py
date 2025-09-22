from ...use_cases.chat_ia_use_case.interfaces import GetPromptInterface
from modules.content_ia.use_cases.dto import UserType
from .free_get_prompt import FreeGetPrompt
from .suscribed_get_prompt import SuscribedGetPrompt
from .premium_get_prompt import PremiumGetPrompt
from .student_get_prompt import StudentGetPrompt

class FactoryGetPrompt:
    def create(self, user_type: UserType) -> GetPromptInterface:
        if user_type.value == UserType.FREE.value:
            return FreeGetPrompt()
        elif user_type.value == UserType.SUSCRIBED.value:
            return SuscribedGetPrompt()
        elif user_type.value == UserType.PREMIUM.value:
            return PremiumGetPrompt()
        elif user_type.value == UserType.STUDENT.value:
            return StudentGetPrompt()