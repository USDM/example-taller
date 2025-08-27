from abc import ABC, abstractmethod
from .factory_user_content import FactoryUserContent
from modules.content_ia.use_cases.dto import UserType

class FactoryCreatorUserContent(ABC):

  @abstractmethod
  def create(self, user_type:UserType) -> FactoryUserContent:
    pass