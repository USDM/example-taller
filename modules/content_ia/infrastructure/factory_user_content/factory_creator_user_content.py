from .factory_user_content import FactoryUserContent
from .free_factory_user_content import FreeFactoryUserContent
from .suscribe_factory_user_content import SuscribeFactoryUserContent
from .pro_factory_user_content import ProFactoryUserContent
from .student_factory_user_content import StudentFactoryUserContent
from modules.content_ia.use_cases.dto import UserType

from modules.content_ia.use_cases.generate_content_use_case.interfaces import FactoryCreatorUserContent as FactoryCreatorUserContentInterface

class FactoryCreatorUserContent(FactoryCreatorUserContentInterface):

  def create(self, user_type:UserType) -> FactoryUserContent:
    if user_type.value == UserType.FREE.value:
        return FreeFactoryUserContent()
    elif user_type.value == UserType.SUSCRIBED.value:
        return SuscribeFactoryUserContent()
    elif user_type.value == UserType.PREMIUM.value:
        return ProFactoryUserContent()
    elif user_type.value == UserType.STUDENT.value:
        return StudentFactoryUserContent()
    else:
        raise ValueError(f"User type {user_type} not supported")