from ...use_cases.dto import UserType
from .interfaces import GetPromptInterface
from .free_get_prompt import FreeGetPrompt
from .subs_get_prompt import SubsGetPrompt
from .pro_get_prompt import ProGetPrompt
from .student_get_prompt import StudentGetPrompt


class GetPromptFactory:
    def create(self, user_type:UserType) -> GetPromptInterface:
        if user_type.value == UserType.FREE.value:
            return FreeGetPrompt()
        elif user_type.value == UserType.SUSCRIBED.value:
            return SubsGetPrompt()
        elif user_type.value == UserType.PREMIUM.value:
            return ProGetPrompt()
        elif user_type.value == UserType.STUDENT.value:
            return StudentGetPrompt()
        else:
            raise ValueError(f"User type {user_type} not supported")