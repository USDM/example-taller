from ...use_cases.generate_content_use_case.interfaces import FactoryGenerateContentIA, GenerateContentIAInterface
from ...use_cases.dto import UserData, UserType
from .generate_content_ia_premium import GenerateContentIAPremium
from .generate_content_ia_free import GenerateContentIAFree
from .generate_content_ia_student import GenerateContentIAStudent
from .generate_content_ia_suscribed import GenerateContentIASuscribed

class FactoryGenerateContentIA(FactoryGenerateContentIA):
    def create_generate_content_ia(self, type_user:UserData) -> GenerateContentIAInterface:
        if type_user.user_type == UserType.PREMIUM.value:
            return GenerateContentIAPremium()
        elif type_user.user_type == UserType.FREE.value:
            return GenerateContentIAFree()
        elif type_user.user_type == UserType.STUDENT.value:
            return GenerateContentIAStudent()
        elif type_user.user_type == UserType.SUSCRIBED.value:
            return GenerateContentIASuscribed()
        
