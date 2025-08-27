from abc import ABC, abstractmethod
from .user_repository import UserRepository

class FactoryUserRepository(ABC):

  @abstractmethod
  def create_using_mode(self, mode:str) -> UserRepository:
    pass