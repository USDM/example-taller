from .memory_user_repository import MemoryUserRepository
from .data_base_user_repository import DataBaseUserRepository
from .user_repository import UserRepository

class FactoryUserRepository:

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