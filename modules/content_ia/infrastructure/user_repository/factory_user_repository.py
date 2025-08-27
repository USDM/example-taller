from modules.content_ia.use_cases.generate_content_use_case.interfaces import UserRepository
from .memory_user_repository import MemoryUserRepository
from .data_base_user_repository import DataBaseUserRepository
from modules.content_ia.use_cases.generate_content_use_case.interfaces import FactoryUserRepository as FactoryUserRepositoryInterface

class FactoryUserRepository(FactoryUserRepositoryInterface):

  def create_using_mode(self, mode:str) -> UserRepository:
    if mode == "test":
      return MemoryUserRepository()
    elif mode == "production" or mode == "development":
      return DataBaseUserRepository()
    else:
      raise ValueError(f"Invalid mode: {mode}")
    
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(FactoryUserRepository, cls).__new__(cls)
    return cls.instance